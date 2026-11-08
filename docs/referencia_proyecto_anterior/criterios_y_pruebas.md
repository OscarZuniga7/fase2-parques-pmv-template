# Matriz de verificación para ejecución real

| CA | Acción | Resultado esperado | Estado inicial | Evidencia a obtener |
|---|---|---|---|---|
| CA-01 | Ingresar como admin y guardar inscripción nueva | 1 fila nueva | PENDIENTE | Captura de formulario + SELECT |
| CA-02 | Repetir excursión/visitante | Rechazo sin duplicación | PENDIENTE | Mensaje y SELECT |
| CA-03 | Completar capacidad, intentar nuevo registro | Mensaje de aforo | PENDIENTE | SELECT cupos y mensaje |
| CA-04 | Ingresar `lector_demo` | Dashboard sí; operaciones no | PENDIENTE | Captura menú |
| CA-05 | Crear/modificar/desactivar parque | Cambios y activo=0 | PENDIENTE | Captura formulario + SELECT |
| CA-06 | Crear/modificar/desactivar especie | Cambios y activo=0 | PENDIENTE | Captura formulario + SELECT |
| CA-07 | Cambiar filtros dashboard | 4 gráficos actualizados | PENDIENTE | Cuatro capturas |
| CA-08 | Ejecutar R1–R12 | 6 vistas + 6 procedures y resultados coherentes | PENDIENTE | 12 capturas Workbench |
| CA-09 | Levantar Docker Compose | mysql healthy + app accesible | PENDIENTE | docker compose ps / Ports |

No marcar pruebas como aprobadas antes de ejecutarlas. Anotar fecha, ejecutor, datos de prueba, resultado real y error si aparece.
