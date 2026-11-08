# Diagnóstico: Fase 1 frente a exigencias de Fase 2

Fuentes: informe de Fase 1 suministrado para revisión privada, y enunciado oficial Caso 1.

| N.º | Situación en Fase 1 | Brecha frente a Fase 2 | Propuesta para discusión |
|---|---|---|---|
| 1 | ROL identifica funciones del trabajador | El PMV exige **dos roles de acceso** | Tabla USUARIO separada de roles laborales; roles `administrador` y `consulta` |
| 2 | MERE tiene comunidad que administra parque; modelo relacional contiene `PARQUE_NATURAL.idTrabajador` | Contradicción conceptual: quién administra el parque | Mantener `codigoComunidad` como administradora y separar `idAdministrador` para trabajador designado; aclarar cardinalidades con el grupo |
| 3 | Especialización de ESPECIE parcial/disjunta | Las vistas requieren clasificación explícita y especies sin clasificar | Agregar atributo tipo para consulta; conservar subtablas; probar exclusividad |
| 4 | INSCRIPCION con FK compuesta a EXCURSION | PMV necesita controlar capacidad y duplicados | Agregar UNIQUE por excursión/visitante; bloqueo en transacción Python |
| 5 | PARQUE y ESPECIE sin atributo de vigencia | CRUD puede requerir retirar registros referenciados | Agregar `activo` para desactivación lógica |
| 6 | Relación INVESTIGA/PROYECTO/PARTICIPA | Vista R7 exige investigadores y especies por proyecto | Mantener las dos tablas puente y probar agregaciones con `COUNT(DISTINCT)` |
| 7 | `EVALUACION` 1:1 opcional respecto de inscripción | Dashboard requiere promedio significativo | Mantener `idInscripcion` como PK/FK, calificación CHECK 1–7, variedad de evaluaciones |
| 8 | Fase 1 solo justifica 3 preguntas | Fase 2 requiere 12 objetos SQL y pregunta adicional | R1–R12 según Sarita; nueva P4 tasa de asistencia por área |
| 9 | Fase 1 contiene 20+ tablas; algunas relaciones circulares | Orden DDL y poblamiento más complejo | Crear parque y trabajador en dos pasos, luego asignar administrador |

**Decisiones por confirmar en clase:** denominación de Comunidad Autónoma en un caso ambientado en Chile; interpretación del tipo `Mineral` dentro de `ESPECIE`; si una inscripción representa asistente efectivo o solo reserva; alcance de regla «solo un parque por trabajador»; reportes del informe antes de modificaciones.

La propuesta **no es una corrección validada por Sarita**, sino una implementación docente para que el grupo la cuestione, contraste y documente.
