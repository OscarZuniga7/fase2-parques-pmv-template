# 🌳 Sistema Integral de Gestión de Parques Naturales

## Proyecto Fase 2 – Caso 1
**UNAB | TDFI103 Bases de Datos | Segundo semestre 2026**

Plantilla docente de demostración para el Proyecto Semestral Fase 2.

> Este repositorio es un ejemplo pedagógico. Cada grupo debe adaptar
> su solución al caso asignado, al MERE corregido y al enunciado
> oficial de la coordinación académica.

---

## 1. Objetivo del proyecto

Construir una solución integrada para la gestión de parques
naturales y conservación ambiental, utilizando una base de datos
relacional MySQL y una aplicación web desarrollada con Python.

La solución incluye:

- Modelo relacional con claves primarias y foráneas.
- Base de datos MySQL 8.4.
- Datos sintéticos de demostración.
- Seis vistas SQL y seis procedimientos almacenados.
- Aplicación web Streamlit.
- Formulario de inscripción a excursiones.
- CRUD de parques naturales y especies.
- Autenticación con roles administrador y lector.
- Dashboard con cuatro preguntas de negocio.
- Despliegue mediante Docker Compose.

## 2. Arquitectura tecnológica

Herramientas principales:

- MySQL 8.x: almacenamiento y procesamiento SQL.
- MySQL Workbench: modelo relacional y evidencias académicas.
- Python 3.12: lógica de aplicación.
- SQLAlchemy y PyMySQL: comunicación con MySQL.
- Streamlit: interfaz web.
- Pandas y Plotly: análisis y gráficos.
- Faker: generación de datos sintéticos.
- Docker Compose: despliegue integrado.

Herramienta complementaria:

- phpMyAdmin: administración y consultas SQL desde el navegador.

**phpMyAdmin no reemplaza a MySQL Workbench** para los
entregables oficiales del curso.

Arquitectura simplificada:

    Usuario
       |
       v
    Streamlit (8501)
       |
       v
    Python + SQLAlchemy
       |
       v
    MySQL 8.4
       ^
       |
    phpMyAdmin (8090)

## 3. Estructura del repositorio

    app/
        main.py             Interfaz Streamlit
        db.py               Conexión a MySQL
        negocio.py          Reglas de negocio
        main_inicial.py     Primera demostración mínima

    sql/
        00_integral.sql
        01_estructura.sql
        02_objetos.sql
        03_ejecutar_requerimientos.sql
        04_verificaciones.sql
        05_datos.sql

    db-init/
        01_estructura.sql
        02_objetos.sql
        03_datos.sql

    docs/
        mere/
        workbench/
        guias/
        evidencias/

    equipo/
        bitacoras/

    scripts/
    tests/

    SPEC.md
    Dockerfile
    docker-compose.yml
    requirements.txt
    .env.example

La carpeta db-init contiene exclusivamente los scripts
que MySQL ejecuta durante la primera inicialización.

La carpeta sql contiene material para revisión académica,
consultas, pruebas y ejecución independiente.

## 4. Crear una copia en GitHub Codespaces

1. Abrir el repositorio en GitHub.
2. Seleccionar "Use this template".
3. Crear un repositorio propio.
4. Abrir "Code" y seleccionar "Codespaces".
5. Crear un Codespace en la rama principal.

En la terminal ejecutar:

    cp .env.example .env

Las contraseñas de .env.example son únicamente demostrativas.
Se deben cambiar cuando corresponda.

Iniciar los servicios:

    docker compose up -d --build

Comprobar:

    docker compose ps

Se esperan tres servicios:

- mysql: saludable (healthy).
- phpmyadmin: en ejecución.
- streamlit: en ejecución.

## 5. Abrir las aplicaciones

En la pestaña PUERTOS de Codespaces:

- Puerto 8501: aplicación Streamlit.
- Puerto 8090: phpMyAdmin.
- Puerto 3307: MySQL local para conexiones compatibles.

Mantener los puertos web privados.

Para phpMyAdmin utilizar el usuario MySQL configurado
en .env.

Para Streamlit se utilizan cuentas de demostración
almacenadas en la tabla usuario:

- admin_demo: administrador.
- lector_demo: consulta.

Las contraseñas de las cuentas de demostración se
documentarán por separado para su uso en clases.

No utilizar estas cuentas en un sistema real.

## 6. Inicialización de MySQL

En la primera ejecución sobre un volumen nuevo, MySQL
procesa automáticamente:

1. db-init/01_estructura.sql
2. db-init/02_objetos.sql
3. db-init/03_datos.sql

De esta forma se cargan las tablas, vistas, procedimientos
y datos sintéticos de demostración.

IMPORTANTE:

Los archivos de db-init solamente se ejecutan cuando
MySQL inicializa un volumen de datos vacío.

No ejecutar sql/00_integral.sql encima de una base
ya inicializada sin revisar previamente sus instrucciones.

No utilizar docker compose down -v sobre bases con
datos que se necesite conservar.

## 7. Funcionalidades del PMV

### 7.1. Inicio de sesión y roles

Administrador:
- Consulta el dashboard.
- Registra inscripciones.
- Administra parques.
- Administra especies.

Lector:
- Consulta el dashboard.
- Accede a consultas básicas.
- No dispone de los formularios administrativos.

Las restricciones de interfaz no sustituyen una
auditoría de seguridad completa.

### 7.2. Inscripciones

El formulario permite seleccionar una excursión
y un visitante existentes.

Contempla comprobaciones de:
- Existencia de la excursión.
- Capacidad disponible.
- Inscripción duplicada.
- Existencia del visitante.
- Integridad transaccional.

### 7.3. CRUD de parques

Permite:
- Consultar.
- Crear.
- Modificar.
- Desactivar lógicamente.

### 7.4. CRUD de especies

Permite:
- Consultar.
- Crear.
- Modificar.
- Desactivar lógicamente.

Al crear especies clasificadas, se considera la
especialización Vegetal, Animal o Mineral.

### 7.5. Dashboard

Contiene cuatro preguntas de negocio:

P1. Áreas con mayor afluencia de visitantes.
P2. Composición de especies inventariadas.
P3. Participación y evaluación de excursiones.
P4. Áreas con menor tasa de asistencia.

Las cuatro visualizaciones utilizan datos de MySQL.

## 8. Requerimientos SQL

Los doce requerimientos se ejecutan separadamente
del PMV y deben documentarse en MySQL Workbench.

Procedimientos almacenados:

- R1: sp_r1_areas_visitantes
- R4: sp_r4_parques_excursiones
- R9: sp_r9_excursiones_sobre_promedio
- R10: sp_r10_especies_sobre_promedio
- R11: sp_r11_visitantes_destacados
- R12: sp_r12_parques_sobre_promedio

Vistas:

- R2: v_r2_distribucion_especies
- R3: v_r3_visitantes_evaluacion
- R5: v_r5_asistencia_area
- R6: v_r6_especies_mayor_inventario
- R7: v_r7_proyectos_investigacion
- R8: v_r8_trabajadores_multifuncion

Ejemplos para phpMyAdmin:

    SELECT * FROM v_r5_asistencia_area;

    CALL sp_r10_especies_sobre_promedio('Vegetal');

    CALL sp_r9_excursiones_sobre_promedio(
        1, '2026-01-01', '2026-12-31'
    );

El procedimiento R10 fue corregido para comparar
totales de inventario por especie con el promedio
de especies del mismo tipo.

## 9. Pruebas docentes realizadas

En la demostración del 8 de noviembre de 2026 se comprobó:

- Inicio de los tres servicios Docker.
- Base MySQL con datos sintéticos.
- Existencia de seis vistas y seis procedimientos.
- Ejecución de los doce objetos SQL en phpMyAdmin.
- Dashboard de cuatro preguntas de negocio.
- Registro de una inscripción.
- Rechazo de una inscripción duplicada.
- Creación, modificación y desactivación de un parque.
- Creación, modificación y desactivación de una especie.
- Persistencia verificada mediante consultas SQL.
- Relación entre especie y subtipo vegetal.
- Inicio de sesión de administrador y lector.
- Restricción de opciones administrativas en la interfaz.

Estas pruebas no sustituyen las evidencias oficiales
que cada equipo debe obtener en MySQL Workbench.

## 10. Entregables académicos pendientes

Cada grupo debe preparar y justificar:

- MERE corregido.
- Modelo relacional en MySQL Workbench.
- Scripts integrales y datos sintéticos.
- Seis vistas y seis procedimientos.
- Evidencias de ejecución en Workbench.
- PMV con sus cuatro funcionalidades.
- Matriz de responsabilidades.
- Bitácoras individuales.
- Informe final y presentación de defensa.

Consultar siempre el PDF oficial de su caso.

## 11. Limitaciones del ejemplo

- Los datos son sintéticos y no deben interpretarse
  como información real de parques o visitantes.
- La distribución de algunos datos es uniforme.
- Existen especies clasificadas como "Sin clasificar";
  debe justificarse su coherencia con el MERE.
- Las reglas de especialización requieren revisión
  adicional frente a modificaciones SQL externas.
- Los accesos de demostración no son adecuados
  para producción.
- Las evidencias y modelos de MySQL Workbench
  todavía deben prepararse.
- El generador Faker debe incorporarse y documentarse
  en esta nueva plantilla.

## 12. Uso responsable de IA

La IA puede apoyar el análisis, el diseño y la programación.

Sin embargo, cada estudiante debe comprender,
probar y explicar su propia solución.

No se deben presentar capturas ficticias ni resultados
que no hayan sido ejecutados realmente.

---

**Plantilla docente UNAB – TDFI103 Bases de Datos**

Caso 1: Sistema Integral de Gestión de Parques Naturales
y Conservación Ambiental.

## 13. Generación reproducible con Faker

El proyecto incluye `app/generar_datos.py`, que utiliza Faker
con configuración regional chilena (`es_CL`).

La generación emplea una semilla fija para facilitar las
pruebas reproducibles.

Para generar un archivo SQL temporal dentro del contenedor:

    docker compose exec \
      -e DATOS_SQL_SALIDA=/tmp/datos_prueba.sql \
      streamlit python app/generar_datos.py

La variable DATOS_SQL_SALIDA permite seleccionar el destino
sin sobrescribir los scripts originales.

### Prueba realizada el 8 de noviembre de 2026

Se ejecutó el generador dos veces, obteniendo:

- 3.731 sentencias SQL por ejecución.
- Archivos de aproximadamente 561 KB.
- Huellas SHA-256 idénticas.

Esto confirma la reproducibilidad en el entorno probado.

IMPORTANTE:

- El generador no carga automáticamente los datos en MySQL.
- Los datos generados son ficticios.
- No ejecutar el generador directamente sobre los scripts
  oficiales sin conservar una copia.
- Las sales deterministas de las contraseñas se utilizan
  exclusivamente para esta demostración educativa.
- En sistemas reales deben emplearse sales aleatorias
  y mecanismos seguros de gestión de credenciales.
