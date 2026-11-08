# Guion de exposición: 10 minutos + 5 minutos de defensa

- 0:00–1:00: caso, roles de participantes, propósito y pregunta de negocio.
- 1:00–2:15: MERE Fase 1 vs. MERE corregido, un cambio importante y motivación.
- 2:15–3:15: modelo final Workbench, PK/FK y una restricción relevante.
- 3:15–4:15: generación Faker, conteos de registros y prueba de integridad.
- 4:15–6:00: 6 vistas y 6 procedures: explicar en pantalla al menos 2 ejemplos, mostrar evidencias de las otras 10 en el informe.
- 6:00–8:30: PMV funcionando: login rol consulta/admin, formulario, CRUD, dashboard.
- 8:30–9:20: Docker y reproducibilidad; `docker compose ps` y puertos.
- 9:20–10:00: conclusiones breves de cada integrante; matriz/bitácora y uso responsable de IA.

## Preguntas de defensa para distintos integrantes
- ¿Por qué `AREA` tiene PK compuesta? ¿Qué ocurre si cambias su parque?
- ¿Por qué `INSCRIPCION` tiene identificador propio y UNIQUE por visitante/excursión?
- ¿En qué se diferencia una vista de un procedimiento con parámetros?
- ¿Qué cambia si una excursión tiene 0 inscripciones? ¿Por qué LEFT JOIN?
- ¿Por qué el dashboard no llama directamente las 6 vistas/procedures evaluadas?
- ¿Dónde se validan las reglas: Streamlit, Python o MySQL?
- ¿Qué muestra `CONTEXT.md` que `SPEC.md` no muestra?
- ¿Qué evidencia demuestra que el `lector_demo` no puede escribir?
- ¿Qué harías si una respuesta generada por IA contradice una regla de negocio?
