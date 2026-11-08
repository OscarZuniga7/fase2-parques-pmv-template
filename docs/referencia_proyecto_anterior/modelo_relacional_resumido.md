# Modelo relacional propuesto · Guía para reconstruir en MySQL Workbench

**No sustituye el diagrama EER obligatorio de Workbench**. El estudiante deberá comprobar cardinalidades y reflejar las correcciones aceptadas.

```mermaid
erDiagram
  COMUNIDAD_AUTONOMA ||--o{ PARQUE_NATURAL : administra
  COMUNIDAD_AUTONOMA ||--o{ COMPARTEN : participa
  PARQUE_NATURAL ||--o{ COMPARTEN : compartido
  PARQUE_NATURAL ||--|{ AREA : contiene
  PARQUE_NATURAL ||--o{ TRABAJADOR : emplea
  ROL ||--o{ TRABAJADOR : desempena
  TRABAJADOR o|--o{ TRABAJADOR : supervisa
  TRABAJADOR ||--o{ TRABAJADOR_FUNCIONES : tiene
  TRABAJADOR ||--o{ TRABAJADOR_CONTACTO : tiene
  TRABAJADOR ||--o| USUARIO : credencial
  PARQUE_NATURAL ||--o{ PROYECTO_CIENTIFICO : organiza
  TRABAJADOR ||--o{ PARTICIPA : investigador
  PROYECTO_CIENTIFICO ||--o{ PARTICIPA : equipo
  PROYECTO_CIENTIFICO ||--o{ INVESTIGA : estudia
  ESPECIE ||--o{ INVESTIGA : estudiada
  ESPECIE ||--o| VEGETAL : subtipo
  ESPECIE ||--o| ANIMAL : subtipo
  ESPECIE ||--o| MINERAL : subtipo
  AREA ||--o{ INVENTARIO_ESPECIE : registra
  ESPECIE ||--o{ INVENTARIO_ESPECIE : inventariada
  AREA ||--o{ EXCURSION : desarrolla
  EXCURSION ||--o{ INSCRIPCION : recibe
  VISITANTE ||--o{ INSCRIPCION : realiza
  INSCRIPCION ||--o| EVALUACION : genera
  PROYECTO_CIENTIFICO ||--o{ SE_DESARROLLA_EN : sucede
  AREA ||--o{ SE_DESARROLLA_EN : ubica
```

`AREA` se identifica con `(numCorrelativo, numInterno)`; `EXCURSION` con `(numCorrelativo, numInterno, codigoExcursion)`; `INSCRIPCION` usa surrogate `idInscripcion`; `EVALUACION` usa esta última como PK y FK. La especialización es parcial y disjunta en el MERE original y requiere refuerzo de integridad global.

**Pendiente para estudiantes:** corregir el MERE en ERDPlus, construir EER Workbench real y obtener capturas legibles.
