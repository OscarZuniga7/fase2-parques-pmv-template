# ESPECIFICACIÓN DEL PROYECTO – FASE 2

## 1. Identificación

Asignatura: TDFI103 – Bases de Datos
Universidad: Universidad Andrés Bello
Semestre: Segundo semestre de 2026

Caso 1: Sistema Integral de Gestión de Parques Naturales
y Conservación Ambiental.

Proyecto docente de demostración y plantilla reutilizable.

## 2. Propósito

Implementar el modelo conceptual y relacional desarrollado
en la Fase 1, incorporando las correcciones necesarias.

Construir una base de datos MySQL funcional y un Producto
Mínimo Viable (PMV) integrado mediante Python y Streamlit.

## 3. Herramientas

- ERDPlus o equivalente: MERE.
- MySQL 8.x: motor de base de datos.
- MySQL Workbench: modelo relacional y evidencias SQL.
- Python 3.12+: desarrollo y generación de datos.
- SQLAlchemy + PyMySQL: conexión a MySQL.
- Faker: datos sintéticos.
- Pandas: análisis de datos.
- Plotly: visualizaciones.
- Streamlit: aplicación web.
- OpenCode: apoyo de IA según taller No-Code.
- Docker y Docker Compose: despliegue.

Complemento pedagógico:
- phpMyAdmin: exploración y ejecución de SQL desde navegador.

phpMyAdmin no sustituye MySQL Workbench en los
entregables exigidos por la coordinación académica.

## 4. Implementación de la base de datos

La solución debe incluir:

- MERE corregido.
- Modelo relacional documentado en MySQL Workbench.
- Tablas, PK, FK y restricciones justificadas.
- Datos sintéticos coherentes y reproducibles.
- Script integral para reconstruir la base desde cero.
- Seis vistas SQL.
- Seis procedimientos almacenados.

## 5. Requerimientos SQL

R1  Procedimiento: áreas con mayor cantidad de visitantes.
R2  Vista: distribución de especies por parque y área.
R3  Vista: participantes y evaluación de excursiones.
R4  Procedimiento: parques con más excursiones y visitantes.
R5  Vista: tasa de asistencia por área.
R6  Vista: especies con mayor cantidad inventariada.
R7  Vista: proyectos de investigación.
R8  Vista: trabajadores que desempeñan múltiples funciones.
R9  Procedimiento: excursiones sobre el promedio del parque.
R10 Procedimiento: especies con inventario superior al
    promedio de las especies de su mismo tipo.
R11 Procedimiento: visitantes destacados por participación
    y evaluación promedio.
R12 Procedimiento: parques con promedio de visitantes
    por excursión superior al promedio general.

Cada objeto SQL debe cumplir las condiciones específicas
establecidas en el PDF oficial del Caso 1.

Las doce consultas son evidencia independiente del PMV.

## 6. Funcionalidades del PMV

El PMV debe integrar cuatro funcionalidades:

1. Formulario transaccional para inscripción de visitantes
   a excursiones, respetando reglas de negocio y FK.

2. CRUD de al menos dos tablas básicas:
   Parque Natural y Especie.

3. Autenticación y autorización de usuarios con roles
   diferenciados.

4. Dashboard con las tres preguntas de negocio de
   Fase 1 y una cuarta pregunta propuesta y justificada.

Todas las funcionalidades deben compartir la misma
base de datos MySQL.

## 7. Reglas de negocio y pruebas

Verificar, entre otras:

- Integridad referencial.
- Restricciones de las claves.
- Capacidad de las excursiones.
- Prevención de inscripciones duplicadas.
- Coherencia de especializaciones de especies.
- Permisos según rol de usuario.
- Persistencia de operaciones CRUD.
- Resultados de vistas y procedimientos.

## 8. Documentación y entregables

- Informe final según PDF oficial.
- Script integral SQL.
- Script de generación de datos.
- Código fuente del PMV.
- Dockerfile y docker-compose.yml.
- Documento de la disertación.
- MERE y modelo relacional.
- Evidencias SQL reales obtenidas en Workbench.
- Matriz de responsabilidades.
- Bitácoras individuales.

## 9. Inteligencia artificial

La IA es una herramienta de apoyo.

Todo código, consulta SQL, resultado, regla de negocio
y decisión técnica debe ser comprendido, probado y
defendido por el equipo.

No se deben inventar evidencias ni resultados.

## 10. Objetivo pedagógico de esta plantilla

Demostrar paso a paso la integración de:

MERE -> Modelo relacional -> MySQL -> SQL ->
Python/Streamlit -> Pruebas -> Aplicación funcional.

La plantilla es un ejemplo de referencia; cada grupo
debe adaptarla a su caso y modelo definitivo.
