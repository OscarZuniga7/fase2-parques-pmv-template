# Prompts escalonados para enseñar Spec-Driven Development

**Prompt 1 · Diagnóstico, no programación:**
«Analiza mi MERE, modelo relacional e informe de Fase 1 junto con el enunciado oficial del Caso N y mi `requerimientos.txt`. NO cambies el modelo todavía. Devuelve una tabla de brechas: regla, problema, cambio propuesto y prueba para validarlo. Distingue requisitos explícitos de supuestos».

**Prompt 2 · Decisión humana:**
«Estos son los cambios que el grupo aprobó en `cambios_bd.md`. Aplica SOLO los aprobados y justifica cualquier efecto en PK, FK, cardinalidades y atributos. Propón el MERE corregido y el modelo MySQL Workbench, sin inventar capturas».

**Prompt 3 · SQL por capas:**
«Lee el SPEC.md y el modelo definitivo. Redacta DDL MySQL 8 con comentarios de restricciones. NO programes todavía Streamlit. Propón pruebas positivas y negativas para cada regla. Espera revisión del grupo».

**Prompt 4 · Datos y requerimientos:**
«Con el DDL probado y los volúmenes del caso, genera datos ficticios con Faker reproducible. Propón R1–R12 diferenciando 6 vistas y 6 procedures. Incluye SELECT/CALL y explica la lógica, pero NO declares que se ejecutaron; el equipo los ejecutará en Workbench».

**Prompt 5 · PMV:**
«Construye el PMV en Python 3.12, Streamlit, SQLAlchemy, PyMySQL, Pandas y Plotly conectado a MySQL; incorpora cuatro funciones integradas (formulario, CRUD de dos tablas, usuarios con dos roles y dashboard con cuatro preguntas). No incluyas como dependencias del dashboard los 6 objetos SQL evaluados. Registra archivos nuevos y decisiones en CONTEXT.md».

**Prompt 6 · Pruebas:**
«Lee SPEC.md y la matriz CA. Propón acciones manuales de prueba y resultados esperados para cada CA, distinguiendo lo que pudiste ejecutar de lo que quedó pendiente. No inventes capturas de Codespaces ni de Workbench».
