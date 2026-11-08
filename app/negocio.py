"""Reglas del negocio centralizadas: la interfaz no ejecuta SQL."""
from sqlalchemy import text
from db import engine

def registrar_inscripcion(parque,area,excursion,visitante,asistencia):
    with engine().begin() as c:
        x=c.execute(text('SELECT capacidad FROM excursion WHERE numCorrelativo=:p AND numInterno=:a AND codigoExcursion=:x AND activo=1 FOR UPDATE'),dict(p=parque,a=area,x=excursion)).scalar_one_or_none()
        if x is None:return False,'La excursión no existe o está inactiva.'
        n=c.execute(text('SELECT COUNT(*) FROM inscripcion WHERE numCorrelativo=:p AND numInterno=:a AND codigoExcursion=:x'),dict(p=parque,a=area,x=excursion)).scalar_one()
        if n>=x:return False,'La excursión alcanzó su capacidad máxima.'
        ya=c.execute(text('SELECT 1 FROM inscripcion WHERE numCorrelativo=:p AND numInterno=:a AND codigoExcursion=:x AND idVisitante=:v'),dict(p=parque,a=area,x=excursion,v=visitante)).first()
        if ya:return False,'El visitante ya está inscrito en esta excursión.'
        exists=c.execute(text('SELECT 1 FROM visitante WHERE idVisitante=:v'),dict(v=visitante)).first()
        if not exists:return False,'El visitante seleccionado no existe.'
        c.execute(text('INSERT INTO inscripcion (numCorrelativo,numInterno,codigoExcursion,idVisitante,asistencia) VALUES (:p,:a,:x,:v,:s)'),dict(p=parque,a=area,x=excursion,v=visitante,s=bool(asistencia)))
        return True,'Inscripción registrada correctamente.'

def guardar_parque(id_,nombre,superficie,presupuesto,comunidad,editar=False):
    if not nombre.strip() or superficie<=0 or presupuesto<0:return False,'Revise nombre, superficie y presupuesto.'
    with engine().begin() as c:
        if editar:
            r=c.execute(text('UPDATE parque_natural SET nombre=:n,superficie=:s,presupuesto=:b,codigoComunidad=:c WHERE numCorrelativo=:i'),dict(n=nombre,s=superficie,b=presupuesto,c=comunidad,i=id_))
        else:
            r=c.execute(text('INSERT INTO parque_natural(numCorrelativo,nombre,superficie,presupuesto,codigoComunidad) VALUES (:i,:n,:s,:b,:c)'),dict(i=id_,n=nombre,s=superficie,b=presupuesto,c=comunidad))
        return (r.rowcount>0),'Registro guardado.'

def guardar_especie(id_,nombre,tipo,editar=False):
    if not nombre.strip() or tipo not in ('Vegetal','Animal','Mineral','Sin clasificar'):return False,'Datos no válidos.'
    with engine().begin() as c:
        # Para edición, no se cambia el tipo de una especie con subtabla existente.
        if editar:
            previo=c.execute(text('SELECT tipo FROM especie WHERE idEspecie=:i'),dict(i=id_)).scalar_one_or_none()
            if previo and previo!=tipo:return False,'No se permite cambiar el tipo sin migrar su especialización.'
            r=c.execute(text('UPDATE especie SET nombreVulgar=:n WHERE idEspecie=:i'),dict(n=nombre,i=id_))
        else:
            r=c.execute(text('INSERT INTO especie(idEspecie,nombreVulgar,tipo) VALUES (:i,:n,:t)'),dict(i=id_,n=nombre,t=tipo))
            if tipo=='Vegetal':c.execute(text('INSERT INTO vegetal(idEspecie) VALUES (:i)'),dict(i=id_))
            if tipo=='Animal':c.execute(text('INSERT INTO animal(idEspecie) VALUES (:i)'),dict(i=id_))
            if tipo=='Mineral':c.execute(text('INSERT INTO mineral(idEspecie) VALUES (:i)'),dict(i=id_))
        return (r.rowcount>0),'Registro guardado.'

def desactivar(tabla,id_col,id_):
    if (tabla,id_col) not in [('parque_natural','numCorrelativo'),('especie','idEspecie')]:raise ValueError('Tabla no permitida')
    return execute_local('UPDATE '+tabla+' SET activo=0 WHERE '+id_col+'=:i',id_)

def execute_local(sql,id_):
    with engine().begin() as c:return c.execute(text(sql),dict(i=id_)).rowcount>0
