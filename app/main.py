"""PMV docente del Caso 1. No usar con datos personales reales ni en producción."""
import hashlib,hmac
from datetime import date
import pandas as pd
import plotly.express as px
import streamlit as st
from sqlalchemy import text
from db import fetch,engine
from negocio import registrar_inscripcion,guardar_parque,guardar_especie,desactivar

st.set_page_config(page_title='Parques Naturales | Fase 2',layout='wide',page_icon='🌳')
st.title('🌳 Sistema Integral de Parques Naturales')
st.caption('UNAB · TDFI103 · Caso 1 · Demostración académica con datos sintéticos')

def clave_valida(password,valor):
    try:
        method,it,salt,expected=valor.split('$')
        if method!='pbkdf2_sha256':return False
        got=hashlib.pbkdf2_hmac('sha256',password.encode(),bytes.fromhex(salt),int(it))
        return hmac.compare_digest(got.hex(),expected)
    except (ValueError,TypeError):return False

def login():
    with st.form('login'):
        user=st.text_input('Usuario');pw=st.text_input('Contraseña',type='password');ok=st.form_submit_button('Ingresar')
    if ok:
        try:
            q=fetch('SELECT usuario,claveHash,rol FROM usuario WHERE usuario=:u AND activo=1',{'u':user})
            if q and clave_valida(pw,q[0]['claveHash']):
                st.session_state['usuario']=user;st.session_state['rol']=q[0]['rol'];st.rerun()
            st.error('Credenciales inválidas')
        except Exception as exc:st.error('La conexión a MySQL no está lista. Verifica los contenedores.');st.caption(type(exc).__name__)

if 'usuario' not in st.session_state:
    st.info('Ingresa con una cuenta de demostración. Las claves están documentadas en el README y deben cambiarse para cualquier uso real.')
    login();st.stop()

role=st.session_state['rol']
with st.sidebar:
    st.write(f"**{st.session_state['usuario']}** · {role}")
    if st.button('Cerrar sesión'):
        for k in ['usuario','rol']:st.session_state.pop(k,None)
        st.rerun()
    opciones=['Dashboard','Consultas básicas']
    if role=='administrador':opciones=['Dashboard','Inscripciones','CRUD de parques','CRUD de especies','Consultas básicas']
    pagina=st.radio('Navegación',opciones)

def tabla(sql,p=None):return pd.DataFrame(fetch(sql,p))

if pagina=='Dashboard':
    st.header('Cuatro preguntas de negocio')
    parques=fetch('SELECT numCorrelativo,nombre FROM parque_natural ORDER BY numCorrelativo')
    opts={p['nombre']:p['numCorrelativo'] for p in parques}
    c1,c2,c3=st.columns(3)
    with c1:desde=st.date_input('Desde',date(2026,1,1))
    with c2:hasta=st.date_input('Hasta',date(2026,12,31))
    with c3:eleccion=st.selectbox('Parque',['Todos']+list(opts))
    if desde>hasta:st.error('La fecha inicial debe ser anterior a la final.');st.stop()
    filtro=' AND p.numCorrelativo=:parque' if eleccion!='Todos' else ''
    params={'inicio':desde,'fin':hasta}
    if eleccion!='Todos':params['parque']=opts[eleccion]
    # Dashboard: SELECT independientes para analítica, no reutiliza las 6 vistas/procedures (requisito oficial).
    d1=tabla('''SELECT CONCAT(p.nombre,' / ',a.nombre) area,COUNT(i.idInscripcion) visitantes FROM parque_natural p JOIN area a ON a.numCorrelativo=p.numCorrelativo JOIN excursion x ON (x.numCorrelativo,x.numInterno)=(a.numCorrelativo,a.numInterno) JOIN inscripcion i ON (i.numCorrelativo,i.numInterno,i.codigoExcursion)=(x.numCorrelativo,x.numInterno,x.codigoExcursion) WHERE x.fecha BETWEEN :inicio AND :fin AND i.asistencia=1'''+filtro+''' GROUP BY p.numCorrelativo,a.numInterno,p.nombre,a.nombre ORDER BY visitantes DESC LIMIT 15''',params)
    st.subheader('P1 · Áreas con mayor afluencia de visitantes')
    if not d1.empty:st.plotly_chart(px.bar(d1,x='visitantes',y='area',orientation='h',title='Asistentes por área'),use_container_width=True)
    else:st.info('No hay datos para el filtro.')
    d2=tabla('''SELECT e.tipo,SUM(i.cantidadInventario) ejemplares FROM inventario_especie i JOIN especie e ON e.idEspecie=i.idEspecie JOIN parque_natural p ON p.numCorrelativo=i.numCorrelativo WHERE 1=1'''+filtro+''' GROUP BY e.tipo ORDER BY ejemplares DESC''',{k:v for k,v in params.items() if k=='parque'})
    st.subheader('P2 · Composición de especies inventariadas')
    if not d2.empty:st.plotly_chart(px.pie(d2,names='tipo',values='ejemplares',title='Distribución de ejemplares'),use_container_width=True)
    d3=tabla('''SELECT CONCAT(x.numCorrelativo,'-',x.numInterno,'-',x.codigoExcursion) excursion,COUNT(DISTINCT CASE WHEN i.asistencia=1 THEN i.idInscripcion END) visitantes,ROUND(AVG(CASE WHEN i.asistencia=1 THEN ev.calificacion END),2) evaluacion FROM excursion x JOIN parque_natural p ON p.numCorrelativo=x.numCorrelativo LEFT JOIN inscripcion i ON (i.numCorrelativo,i.numInterno,i.codigoExcursion)=(x.numCorrelativo,x.numInterno,x.codigoExcursion) LEFT JOIN evaluacion ev ON ev.idInscripcion=i.idInscripcion WHERE x.fecha BETWEEN :inicio AND :fin'''+filtro+''' GROUP BY x.numCorrelativo,x.numInterno,x.codigoExcursion HAVING evaluacion IS NOT NULL''',params)
    st.subheader('P3 · Visitantes y evaluación promedio por excursión')
    if not d3.empty:
        st.plotly_chart(px.scatter(d3,x='visitantes',y='evaluacion',hover_name='excursion',title='Participación versus satisfacción'),use_container_width=True)
        st.dataframe(d3,use_container_width=True)
    st.subheader('P4 · ¿Qué áreas tienen menor tasa de asistencia?')
    st.caption('Pregunta nueva: identificar áreas con ausencias elevadas para revisar recordatorios y logística.')
    d4=tabla('''SELECT CONCAT(p.nombre,' / ',a.nombre) area,COUNT(i.idInscripcion) inscritos, SUM(CASE WHEN i.asistencia=1 THEN 1 ELSE 0 END) asistentes, ROUND(100*SUM(CASE WHEN i.asistencia=1 THEN 1 ELSE 0 END)/NULLIF(COUNT(i.idInscripcion),0),2) tasa FROM parque_natural p JOIN area a ON a.numCorrelativo=p.numCorrelativo JOIN excursion x ON (x.numCorrelativo,x.numInterno)=(a.numCorrelativo,a.numInterno) JOIN inscripcion i ON (i.numCorrelativo,i.numInterno,i.codigoExcursion)=(x.numCorrelativo,x.numInterno,x.codigoExcursion) WHERE x.fecha BETWEEN :inicio AND :fin'''+filtro+''' GROUP BY p.numCorrelativo,a.numInterno,p.nombre,a.nombre HAVING inscritos>0 ORDER BY tasa ASC LIMIT 15''',params)
    if not d4.empty:st.plotly_chart(px.bar(d4,x='area',y='tasa',title='Porcentaje de asistencia (menor a mayor)'),use_container_width=True)

elif pagina=='Inscripciones':
    st.header('Formulario transaccional · Inscribir visitante')
    exc=fetch('SELECT numCorrelativo,numInterno,codigoExcursion,fecha,capacidad FROM excursion WHERE activo=1 ORDER BY fecha LIMIT 250')
    vis=fetch('SELECT idVisitante,nombre FROM visitante ORDER BY idVisitante')
    if not exc or not vis:st.warning('Primero ejecuta el script de datos sintéticos.');st.stop()
    exopt={f"Parque {r['numCorrelativo']} / Área {r['numInterno']} / Exc {r['codigoExcursion']} / {r['fecha']}":r for r in exc}
    vopt={f"{r['idVisitante']} · {r['nombre']}":r['idVisitante'] for r in vis}
    with st.form('registro'):
        ex=st.selectbox('Excursión existente',list(exopt));v=st.selectbox('Visitante existente',list(vopt));asis=st.checkbox('Asistió a la excursión',value=False)
        submit=st.form_submit_button('Registrar inscripción')
    if submit:
        r=exopt[ex]
        try:
            ok,msg=registrar_inscripcion(r['numCorrelativo'],r['numInterno'],r['codigoExcursion'],vopt[v],asis)
            (st.success if ok else st.warning)(msg)
        except Exception as exc:st.error(f'Error al registrar: {type(exc).__name__}. Revisa restricciones de integridad.')
    st.caption('Validaciones en Python + FK/UNIQUE en MySQL; control de capacidad con bloqueo transaccional.')

elif pagina=='CRUD de parques':
    st.header('CRUD 1 · Parques naturales')
    st.dataframe(tabla('SELECT numCorrelativo,nombre,superficie,presupuesto,codigoComunidad,activo FROM parque_natural ORDER BY numCorrelativo'),use_container_width=True)
    comunidades=fetch('SELECT codigoComunidad,nombre FROM comunidad_autonoma ORDER BY codigoComunidad')
    codigos={c['nombre']:c['codigoComunidad'] for c in comunidades}
    with st.form('parques'):
        oper=st.radio('Operación',['Crear','Modificar','Desactivar'],horizontal=True)
        id_=st.number_input('ID parque',min_value=1,step=1);nombre=st.text_input('Nombre');sup=st.number_input('Superficie',min_value=0.0,value=150.0);pres=st.number_input('Presupuesto',min_value=0.0,value=100000.0)
        comunidad=st.selectbox('Comunidad administradora',list(codigos));guardar=st.form_submit_button('Aplicar operación')
    if guardar:
        try:
            if oper=='Desactivar':ok=desactivar('parque_natural','numCorrelativo',int(id_));msg='Desactivación lógica completada.'
            else:ok,msg=guardar_parque(int(id_),nombre,float(sup),float(pres),codigos[comunidad],oper=='Modificar')
            (st.success if ok else st.warning)(msg)
        except Exception as exc:st.error(f'No se pudo completar: {type(exc).__name__}. Revisa PK y FK.')
    st.caption('Consultar, crear, modificar y desactivar; la eliminación física se evita por integridad referencial.')

elif pagina=='CRUD de especies':
    st.header('CRUD 2 · Especies')
    st.dataframe(tabla('SELECT idEspecie,nombreVulgar,tipo,activo FROM especie ORDER BY idEspecie'),use_container_width=True)
    with st.form('especies'):
        oper=st.radio('Operación',['Crear','Modificar','Desactivar'],horizontal=True)
        id_=st.number_input('ID especie',min_value=1,step=1);nombre=st.text_input('Nombre vulgar');tipo=st.selectbox('Tipo',['Vegetal','Animal','Mineral','Sin clasificar']);guardar=st.form_submit_button('Aplicar operación')
    if guardar:
        try:
            if oper=='Desactivar':ok=desactivar('especie','idEspecie',int(id_));msg='Desactivación lógica completada.'
            else:ok,msg=guardar_especie(int(id_),nombre,tipo,oper=='Modificar')
            (st.success if ok else st.warning)(msg)
        except Exception as exc:st.error(f'No se pudo completar: {type(exc).__name__}. Revisa PK y FK.')

elif pagina=='Consultas básicas':
    st.header('Consultas de apoyo para navegación')
    st.info('Las 6 vistas y los 6 procedimientos se evalúan aparte en Workbench; no se exponen como funciones del PMV.')
    st.dataframe(tabla('SELECT numCorrelativo,nombre,estadoConservacion,presupuesto FROM parque_natural ORDER BY nombre'),use_container_width=True)
