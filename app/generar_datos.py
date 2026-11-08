"""Genera datos sintéticos reproducibles (NO personas reales). Ejecutar: python app/generar_datos.py"""
import random
from pathlib import Path
from datetime import date, timedelta
from faker import Faker

random.seed(20261107)
fake=Faker('es_CL'); Faker.seed(20261107)
import os
out=Path(os.environ.get(
    'DATOS_SQL_SALIDA',
    str(Path(__file__).resolve().parents[1]/'sql'/'05_datos.sql')
))
rows=['USE parques;', 'SET NAMES utf8mb4;']
def esc(x):
    if x is None:return 'NULL'
    if isinstance(x,bool):return '1' if x else '0'
    if isinstance(x,(int,float)):return str(x)
    return "'"+str(x).replace('\\','\\\\').replace("'","''")+"'"
def ins(tab,cols,vals):
    rows.append('INSERT INTO '+tab+' ('+','.join(cols)+') VALUES ('+','.join(esc(v) for v in vals)+');')
for i,s in enumerate(['Guardaparque','Investigación','Administración','Conservación'],1):ins('rol',['idRol','nombreRol'],[i,s])
for c in range(1,9):ins('comunidad_autonoma',['codigoComunidad','nombre','organismoResp','regionAdmin'],[c,f'Comunidad ambiental {c}',f'Corporación {c}',f'Región {c}'])
for p in range(1,17):
    ins('parque_natural',['numCorrelativo','nombre','superficie','fechaDeclaracion','anioDeclaracion','estadoConservacion','presupuesto','codigoComunidad'],[p,f'Parque Natural Demostración {p}',round(random.uniform(200,3000),2),f'200{p%10}-03-15',2000+p%10,random.choice(['Protegido','En recuperación','Vulnerable']),round(random.uniform(1e6,8e7),2),(p%8)+1]);
    for a in range(1,4):ins('area',['numCorrelativo','numInterno','nombre','estadoOperativo','nivelAcceso','extension'],[p,a,f'Área {p}-{a}',random.choice(['Activa','En mantenimiento']),random.choice(['Libre','Guiado','Restringido']),random.randint(30,400)])
    for c in [(p%8)+1,((p+1)%8)+1]:ins('comparten',['numCorrelativo','codigoComunidad','porcentajeTerritorial'],[p,c,60 if c==p%8+1 else 40])
for t in range(1,65):ins('trabajador',['idTrabajador','nombre','direccion','fechaNacimiento','estadoCuenta','idRol','idSupervisor','numCorrelativo'],[t,fake.name(),fake.street_address(),'1988-05-09','Activo',(t%4)+1,None if t<=16 else t-16,((t-1)%16)+1]);
for p in range(1,17):rows.append(f'UPDATE parque_natural SET idAdministrador={p} WHERE numCorrelativo={p};')
for t in range(1,65):
    for f in random.sample(['Vigilancia','Conservación','Educación','Investigación','Administración'],random.choice([1,2,3])):ins('trabajador_funciones',['idTrabajador','funcion'],[t,f])
    ins('trabajador_contacto',['idTrabajador','contacto'],[t,f'contacto{t}@example.org'])
for e in range(1,97):
    tipo=['Vegetal','Animal','Mineral','Sin clasificar'][(e-1)%4]
    ins('especie',['idEspecie','estadoConservacion','fechaIncorporacion','nombreVulgar','denominacionCientifica','tipo'],[e,'Estable','2026-01-15',f'Especie ficticia {e}',f'Species fictitia {e}',tipo])
    if tipo=='Vegetal':ins('vegetal',['idEspecie','floracion'],[e,'Primavera'])
    elif tipo=='Animal':ins('animal',['idEspecie','alimentacion','periodoCelo'],[e,'Omnívoro','Estacional'])
    elif tipo=='Mineral':ins('mineral',['idEspecie','caracteristicasMineral','rocas','cristales'],[e,'Muestra educativa','Ígneas','Cuarzo'])
for j in range(1,33):
    p=((j-1)%16)+1
    ins('proyecto_cientifico',['idProyecto','nombre','objetivo','numCorrelativo'],[j,f'Investigación {j}',f'Inventario y conservación {j}',p])
    for t in random.sample(range(1,65),3):ins('participa',['idTrabajador','idProyecto'],[t,j])
    for e in random.sample(range(1,97),3):ins('investiga',['idProyecto','idEspecie'],[j,e])
    ins('se_desarrolla_en',['idProyecto','numCorrelativo','numInterno'],[j,p,random.randint(1,3)])
for k in range(1,385):
    p=random.randint(1,16);a=random.randint(1,3)
    ins('inventario_especie',['codigoInventario','cantidadInventario','fechaUltimoMonitoreo','observaciones','idEspecie','numCorrelativo','numInterno'],[k,random.randint(1,95),'2026-10-01','Dato generado',random.randint(1,96),p,a])
for v in range(1,221):ins('visitante',['idVisitante','nombre','contacto','fechaNacimiento'],[v,fake.name(),f'visitante{v}@example.org','1990-05-12'])
exc=[]
for x in range(1,177):
    p=((x-1)%16)+1;a=(x%3)+1;codigo=x
    dt=date(2026,1,1)+timedelta(days=(x*2)%330)
    cap=random.randint(10,20)
    ins('excursion',['numCorrelativo','numInterno','codigoExcursion','modalidad','horario','fecha','capacidad'],[p,a,codigo,random.choice(['Senderismo','Observación','Educativa']),'09:00:00',str(dt),cap]);exc.append((p,a,codigo,dt,cap))
idx=0
for p,a,codigo,dt,cap in exc:
    count=random.randint(5,min(cap,10))
    for v in random.sample(range(1,221),count):
        idx+=1;asistencia=random.random()<0.8
        ins('inscripcion',['idInscripcion','numCorrelativo','numInterno','codigoExcursion','idVisitante','asistencia','observaciones'],[idx,p,a,codigo,v,asistencia,'Registro sintético'])
        if asistencia and random.random()<0.73:ins('evaluacion',['idInscripcion','numCorrelativoEval','fecha','calificacion','comentario'],[idx,idx,str(dt),round(random.uniform(3.0,7.0),1),'Evaluación ficticia'])
# Contraseñas de DEMO: hashes derivados del hash Python estándar PBKDF2, SIN contraseñas en SQL.
import hashlib
for u,role,worker,pw in [('admin_demo','administrador',1,'DemoAdmin2026!'),('lector_demo','consulta',2,'DemoLector2026!')]+[(f'usuario_demo_{i}', 'consulta', i, f'BloqueadoDemo{i:02d}!') for i in range(3,65)]:
    salt=hashlib.sha256(f'demo-20261107-{u}'.encode()).digest()[:16].hex();h=hashlib.pbkdf2_hmac('sha256',pw.encode(),bytes.fromhex(salt),250000).hex();ins('usuario',['usuario','claveHash','rol','idTrabajador'],[u,f'pbkdf2_sha256$250000${salt}${h}',role,worker])
out.write_text('\n'.join(rows)+'\n',encoding='utf-8')
print(f'{len(rows)} sentencias SQL generadas en {out}')
