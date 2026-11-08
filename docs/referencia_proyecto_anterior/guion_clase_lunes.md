# Guion docente · Lunes 9 de noviembre · NRC 12142 / NRC 12144

## Propósito de 90 minutos de demostración guiada
Al terminar, cada estudiante explica cómo el MERE de Fase 1 se convierte en una aplicación Streamlit, identifica las 12 evidencias SQL y reconoce qué debe quedar en informe, bitácora y defensa.

| Tiempo | Profesor muestra | Estudiantes elaboran / registran |
|---|---|---|
| 0–10 min | Contraste **enunciado oficial vs. taller No-Code**. Stack obligatorio MySQL + Streamlit (no SQLite/Tkinter). | Abren el enunciado de su caso y listan entregables. |
| 10–20 min | MERE y modelo relacional de Fase 1 del Grupo 1; ejemplo de inconsistencia de administrador. | 2 brechas de sus propios modelos; NO cambiar aún. |
| 20–30 min | Diagnóstico IA → `cambios_bd.md` → MERE final + Workbench. | Aceptar/rechazar cambios y justificar. |
| 30–42 min | `01_estructura.sql` y `05_datos.sql`: FK, CHECK, UNIQUE; conteos con MySQL. | Identificar una regla que se valida dos veces. |
| 42–55 min | R1 `CALL` + R2 `SELECT view`: diferencia procedimientos/vistas. Mostrar dónde están R1–R12. | Cada grupo selecciona un R y señala tablas / filtros. |
| 55–68 min | Streamlit 8501: login de 2 roles, crear inscripción, desactivar parque, ver especie. | Describir frontend, negocio y persistencia. |
| 68–78 min | Dashboard: P1, P2, P3 y P4 con filtros; consultas separadas de R1–R12. | Escribir su cuarta pregunta de negocio y decisión asociada. |
| 78–88 min | `SPEC.md`, `CONTEXT.md`, matriz y bitácoras; evaluación individual en defensa. | Distribuir roles, estimar tareas y registrar 1 bitácora. |
| 88–90 min | Resumen: pendiente 20/11 según guía de Álvaro, confirmar en Canvas/syllabus. | Lista de próximos pasos. |

## Orden sugerido de ventanas
1. Mostrar enunciado oficial: 6 views, 6 procedures y PMV integrado.
2. diagramas de Fase 1 de uso interno.
3. `docs/diagnostico_fase1.md` y `docs/cambios_bd.md`.
4. `docs/requerimientos.txt` → `docs/mapa_capas.txt` → `SPEC.md`.
5. Docker `docker compose ps` → phpMyAdmin/Workbench → Streamlit puerto 8501.
6. `sql/03_ejecutar_requerimientos.sql` → `sql/04_verificaciones.sql`.
7. `docs/criterios_y_pruebas.md` → `docs/matriz_responsabilidades.md` → `docs/bitacoras_ejemplo.md`.

## Advertencias que conviene verbalizar
- «La IA no adivina el negocio; muestra un primer resultado y ustedes lo contrastan».
- «No es correcto exhibir SQL que no han ejecutado ni resultados que no han contrastado».
- «La responsabilidad es grupal aunque cada parte tenga un líder».
- «Hay 3 integrantes en este grupo y 4 funcionalidades con distinto responsable exigido: debo confirmar con Sarita cómo resolverlo».
- «No se exige que copien este caso: es una guía metodológica; adapten su propia Fase 1».
