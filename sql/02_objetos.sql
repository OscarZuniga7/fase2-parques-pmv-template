USE parques;
-- Vistas R2, R3, R5, R6, R7, R8. No se usan como sustituto del dashboard.
CREATE OR REPLACE VIEW v_r2_distribucion_especies AS
SELECT p.numCorrelativo, p.nombre parque,a.numInterno,a.nombre area,e.tipo,COUNT(DISTINCT e.idEspecie) especies,SUM(i.cantidadInventario) ejemplares
FROM inventario_especie i JOIN especie e ON e.idEspecie=i.idEspecie JOIN area a ON a.numCorrelativo=i.numCorrelativo AND a.numInterno=i.numInterno JOIN parque_natural p ON p.numCorrelativo=a.numCorrelativo
GROUP BY p.numCorrelativo,p.nombre,a.numInterno,a.nombre,e.tipo;
CREATE OR REPLACE VIEW v_r3_visitantes_evaluacion AS
SELECT x.numCorrelativo,x.numInterno,x.codigoExcursion,x.fecha,COUNT(DISTINCT CASE WHEN i.asistencia=1 THEN i.idInscripcion END) participantes,ROUND(AVG(CASE WHEN i.asistencia=1 THEN ev.calificacion END),2) evaluacionPromedio
FROM excursion x LEFT JOIN inscripcion i ON (i.numCorrelativo,i.numInterno,i.codigoExcursion)=(x.numCorrelativo,x.numInterno,x.codigoExcursion)
LEFT JOIN evaluacion ev ON ev.idInscripcion=i.idInscripcion
GROUP BY x.numCorrelativo,x.numInterno,x.codigoExcursion,x.fecha;
CREATE OR REPLACE VIEW v_r5_asistencia_area AS
SELECT a.numCorrelativo,a.numInterno,a.nombre area,COUNT(i.idInscripcion) inscritos,SUM(CASE WHEN i.asistencia=1 THEN 1 ELSE 0 END) asistentes,
ROUND(100*SUM(CASE WHEN i.asistencia=1 THEN 1 ELSE 0 END)/NULLIF(COUNT(i.idInscripcion),0),2) tasaAsistencia
FROM area a LEFT JOIN excursion x ON (x.numCorrelativo,x.numInterno)=(a.numCorrelativo,a.numInterno)
LEFT JOIN inscripcion i ON (i.numCorrelativo,i.numInterno,i.codigoExcursion)=(x.numCorrelativo,x.numInterno,x.codigoExcursion)
GROUP BY a.numCorrelativo,a.numInterno,a.nombre;
CREATE OR REPLACE VIEW v_r6_especies_mayor_inventario AS
SELECT p.nombre parque,a.nombre area,e.idEspecie,e.nombreVulgar,e.tipo,SUM(i.cantidadInventario) totalInventariado
FROM inventario_especie i JOIN especie e ON e.idEspecie=i.idEspecie JOIN area a ON (a.numCorrelativo,a.numInterno)=(i.numCorrelativo,i.numInterno)
JOIN parque_natural p ON p.numCorrelativo=a.numCorrelativo
GROUP BY p.nombre,a.nombre,e.idEspecie,e.nombreVulgar,e.tipo;
CREATE OR REPLACE VIEW v_r7_proyectos_investigacion AS
SELECT pc.idProyecto,pc.nombre proyecto,p.nombre parque,COUNT(DISTINCT pt.idTrabajador) investigadores,COUNT(DISTINCT inv.idEspecie) especiesEstudiadas
FROM proyecto_cientifico pc JOIN parque_natural p ON p.numCorrelativo=pc.numCorrelativo
LEFT JOIN participa pt ON pt.idProyecto=pc.idProyecto LEFT JOIN investiga inv ON inv.idProyecto=pc.idProyecto
GROUP BY pc.idProyecto,pc.nombre,p.nombre HAVING COUNT(DISTINCT pt.idTrabajador)>=1 AND COUNT(DISTINCT inv.idEspecie)>=1;
CREATE OR REPLACE VIEW v_r8_trabajadores_multifuncion AS
SELECT t.idTrabajador,t.nombre trabajador,p.nombre parque,COUNT(DISTINCT f.funcion) totalFunciones,GROUP_CONCAT(DISTINCT f.funcion ORDER BY f.funcion SEPARATOR ', ') funciones
FROM trabajador t JOIN parque_natural p ON p.numCorrelativo=t.numCorrelativo JOIN trabajador_funciones f ON f.idTrabajador=t.idTrabajador
GROUP BY t.idTrabajador,t.nombre,p.nombre HAVING COUNT(DISTINCT f.funcion)>1;
DELIMITER $$
CREATE PROCEDURE sp_r1_areas_visitantes(IN desde DATE,IN hasta DATE)
BEGIN
SELECT p.nombre parque,a.nombre area,COUNT(DISTINCT i.idInscripcion) visitantes
FROM parque_natural p JOIN area a ON a.numCorrelativo=p.numCorrelativo JOIN excursion x ON (x.numCorrelativo,x.numInterno)=(a.numCorrelativo,a.numInterno)
JOIN inscripcion i ON (i.numCorrelativo,i.numInterno,i.codigoExcursion)=(x.numCorrelativo,x.numInterno,x.codigoExcursion)
WHERE x.fecha BETWEEN desde AND hasta AND i.asistencia=1 GROUP BY p.nombre,a.numCorrelativo,a.numInterno,a.nombre ORDER BY visitantes DESC;
END$$
CREATE PROCEDURE sp_r4_parques_excursiones(IN desde DATE,IN hasta DATE)
BEGIN
SELECT p.numCorrelativo,p.nombre parque,COUNT(DISTINCT CONCAT(x.numCorrelativo,'-',x.numInterno,'-',x.codigoExcursion)) excursiones,
COUNT(DISTINCT CASE WHEN i.asistencia=1 THEN i.idInscripcion END) visitantes
FROM parque_natural p JOIN area a ON a.numCorrelativo=p.numCorrelativo JOIN excursion x ON (x.numCorrelativo,x.numInterno)=(a.numCorrelativo,a.numInterno)
LEFT JOIN inscripcion i ON (i.numCorrelativo,i.numInterno,i.codigoExcursion)=(x.numCorrelativo,x.numInterno,x.codigoExcursion)
WHERE x.fecha BETWEEN desde AND hasta GROUP BY p.numCorrelativo,p.nombre ORDER BY visitantes DESC;
END$$
CREATE PROCEDURE sp_r9_excursiones_sobre_promedio(IN parque_id INT,IN desde DATE,IN hasta DATE)
BEGIN
SELECT v.* FROM v_r3_visitantes_evaluacion v WHERE v.numCorrelativo=parque_id AND v.fecha BETWEEN desde AND hasta
AND v.participantes > (SELECT AVG(v2.participantes) FROM v_r3_visitantes_evaluacion v2 WHERE v2.numCorrelativo=v.numCorrelativo AND v2.fecha BETWEEN desde AND hasta) ORDER BY v.participantes DESC;
END$$
CREATE PROCEDURE sp_r10_especies_sobre_promedio(IN tipo_especie VARCHAR(20))
BEGIN
    SELECT
        e.idEspecie,
        e.nombreVulgar,
        e.tipo,
        SUM(i.cantidadInventario) AS totalInventariado,
        ROUND((
            SELECT AVG(t.totalEspecie)
            FROM (
                SELECT
                    e2.idEspecie,
                    e2.tipo,
                    SUM(i2.cantidadInventario) AS totalEspecie
                FROM especie e2
                JOIN inventario_especie i2
                    ON i2.idEspecie = e2.idEspecie
                GROUP BY e2.idEspecie, e2.tipo
            ) AS t
            WHERE t.tipo = tipo_especie
        ), 2) AS promedioTipo,
        GROUP_CONCAT(
            DISTINCT CONCAT(p.nombre, ' / ', a.nombre)
            ORDER BY p.nombre, a.nombre
            SEPARATOR '; '
        ) AS ubicaciones
    FROM especie e
    JOIN inventario_especie i
        ON i.idEspecie = e.idEspecie
    JOIN area a
        ON a.numCorrelativo = i.numCorrelativo
       AND a.numInterno = i.numInterno
    JOIN parque_natural p
        ON p.numCorrelativo = a.numCorrelativo
    WHERE e.tipo = tipo_especie
    GROUP BY e.idEspecie, e.nombreVulgar, e.tipo
    HAVING totalInventariado > promedioTipo
    ORDER BY totalInventariado DESC;
END$$
CREATE PROCEDURE sp_r11_visitantes_destacados(IN desde DATE,IN hasta DATE)
BEGIN
SELECT v.idVisitante,v.nombre,COUNT(DISTINCT i.idInscripcion) excursiones,ROUND(AVG(ev.calificacion),2) evaluacionMedia
FROM visitante v JOIN inscripcion i ON i.idVisitante=v.idVisitante JOIN excursion x ON (x.numCorrelativo,x.numInterno,x.codigoExcursion)=(i.numCorrelativo,i.numInterno,i.codigoExcursion)
JOIN evaluacion ev ON ev.idInscripcion=i.idInscripcion WHERE x.fecha BETWEEN desde AND hasta AND i.asistencia=1
GROUP BY v.idVisitante,v.nombre
HAVING excursiones > (SELECT AVG(z.n) FROM (SELECT COUNT(DISTINCT i2.idInscripcion) n FROM visitante v2 LEFT JOIN inscripcion i2 ON i2.idVisitante=v2.idVisitante LEFT JOIN excursion x2 ON (x2.numCorrelativo,x2.numInterno,x2.codigoExcursion)=(i2.numCorrelativo,i2.numInterno,i2.codigoExcursion) AND x2.fecha BETWEEN desde AND hasta AND i2.asistencia=1 WHERE x2.fecha IS NOT NULL GROUP BY v2.idVisitante) z)
AND evaluacionMedia > (SELECT AVG(ev2.calificacion) FROM evaluacion ev2 JOIN inscripcion i3 ON i3.idInscripcion=ev2.idInscripcion JOIN excursion x3 ON (x3.numCorrelativo,x3.numInterno,x3.codigoExcursion)=(i3.numCorrelativo,i3.numInterno,i3.codigoExcursion) WHERE x3.fecha BETWEEN desde AND hasta)
ORDER BY excursiones DESC;
END$$
CREATE PROCEDURE sp_r12_parques_sobre_promedio(IN desde DATE,IN hasta DATE)
BEGIN
SELECT p.numCorrelativo,p.nombre parque,ROUND(AVG(v.participantes),2) promedioVisitantes
FROM parque_natural p JOIN v_r3_visitantes_evaluacion v ON v.numCorrelativo=p.numCorrelativo WHERE v.fecha BETWEEN desde AND hasta
GROUP BY p.numCorrelativo,p.nombre
HAVING promedioVisitantes > (SELECT AVG(z.promedio) FROM (SELECT v2.numCorrelativo,AVG(v2.participantes) promedio FROM v_r3_visitantes_evaluacion v2 WHERE v2.fecha BETWEEN desde AND hasta GROUP BY v2.numCorrelativo) z)
ORDER BY promedioVisitantes DESC;
END$$
DELIMITER ;
