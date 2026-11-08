# SPEC.md — PMV Parques Naturales (Ejemplo docente)

## 0. Instrucciones a la IA
Lee primero `docs/requerimientos.txt`, `docs/mapa_capas.txt`, `docs/cambios_bd.md` y el enunciado oficial. Explica dudas y supuestos antes de modificar. Cambia capa por capa (BD, negocio, Streamlit). No inventes evidencias ni resultados. Documenta en CONTEXT.md qué se creó, qué se probó y qué permanece pendiente. Respeta el stack obligatorio.

## 1. Propósito y objetivos
Ver `docs/requerimientos.txt`. Caso: inscripción de visitantes, gestión de parques y especies, analítica de conservación, usuarios/roles.

## 2. Usuarios y roles
**Administrador**: puede crear y modificar registros, registrar inscripciones y consultar dashboard. **Consulta**: solo lectura del dashboard y listados. El permiso se impone en el menú y la ejecución de las páginas.

## 3. Historias de usuario
- HU-01: Como administrador, quiero inscribir un visitante en una excursión, para gestionar cupos y asistencia.
- HU-02: Como administrador, quiero actualizar y desactivar parques, para mantener información sin perder relaciones históricas.
- HU-03: Como administrador, quiero gestionar especies, para registrar inventario y clasificación.
- HU-04: Como investigador, quiero filtrar gráficos por parque y fechas, para identificar zonas prioritarias.
- HU-05: Como usuario de consulta, quiero observar indicadores sin poder editar, para acceder a información autorizada.

## 4. Requerimientos y reglas
RF-01 a RF-06, RNF-01 a RNF-03, R-01 a R-02 y RN-01 a RN-05 se definen en `docs/requerimientos.txt`.

## 5. Front-end
Streamlit: login, inscripciones, CRUD de 2 tablas, dashboard 4 preguntas, consultas básicas. Navegación por rol. Plotly para gráficos, Pandas para tablas.

## 6. Back-end
`app/negocio.py`: validaciones, transacciones, consultas parametrizadas, no en el navegador. `app/db.py`: conexión SQLAlchemy con URL por variables de entorno. A diferencia del stack Tkinter, Streamlit ejecuta Python del lado servidor.

## 7. Base de datos
MySQL 8.4. Ver `sql/01_estructura.sql`, `sql/02_objetos.sql`, `sql/05_datos.sql`. Especializaciones de ESPECIE, entidad débil AREA y EXCURSION, relación INSCRIPCION-EVALUACION 1:0..1.

## 8. Criterios de aceptación
- CA-01: registrar inscripción normal -> queda guardada y asociada a visitante/excursión.
- CA-02: intentar duplicar excursión/visitante -> rechazo claro, ninguna fila nueva.
- CA-03: intentar exceder capacidad -> rechazo claro, ninguna fila nueva.
- CA-04: usuario consulta intenta acceder a formularios de escritura -> no puede.
- CA-05: modificar parque válido -> cambio visible; desactivar -> activo=0.
- CA-06: modificar especie válido -> cambio visible; desactivar -> activo=0.
- CA-07: cuatro gráficos muestran resultados no triviales y sus filtros operan.
- CA-08: `information_schema` contiene 6 vistas y 6 procedures y R1–R12 se ejecutan.
- CA-09: la instalación funciona desde Docker y permite conexión a la misma BD.

## 9. Documentación de cambios
Registrar cada acción de IA en `CONTEXT.md` con fecha, archivos, motivo, verificación real y asuntos pendientes. Los cambios de modelamiento primero se acuerdan en `docs/cambios_bd.md`.
