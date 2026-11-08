# Control de cambios al modelo: ejemplo de revisión (el grupo debe ratificar)

| Cambio | Antes | Después | Motivación | Estado |
|---|---|---|---|---|
| C01 | `PARQUE_NATURAL` sin referencia a comunidad en el modelo relacional | `codigoComunidad` obligatorio | Regla F1: comunidad administra parques | Propuesto |
| C02 | `PARQUE_NATURAL.idTrabajador` | `idAdministrador` opcional/único + `codigoComunidad` | Desambiguar administración territorial y gestión operativa | Propuesto |
| C03 | No existe control de acceso al PMV | `USUARIO` con hash PBKDF2 y 2 roles | Mínimo oficial de control de usuarios | Propuesto |
| C04 | No existe clasificación simple consultable en ESPECIE | Columna `tipo` + subtablas de especialización | R2/R10 y especies sin clasificar | Propuesto |
| C05 | No hay protección frente a inscripción duplicada | UNIQUE en la combinación excursión/visitante | Integridad transaccional del PMV | Propuesto |
| C06 | No hay vigencia lógica | `activo` en PARQUE y ESPECIE | CRUD sin eliminación física de referencias | Propuesto |
| C07 | Falta validación de calificaciones | CHECK de 1 a 7 | Reporte significativo de evaluaciones | Propuesto |

**Tarea docente:** discutir y aprobar/rechazar cada cambio en clase antes de considerar definitivo el MERE. Actualizar los diagramas en ERDPlus y MySQL Workbench; los PNG de Fase 1 no son diagramas definitivos.
