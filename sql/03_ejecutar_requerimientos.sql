USE parques;
-- Ejecutar en Workbench; capturar resultados reales, no inventar capturas.
CALL sp_r1_areas_visitantes('2026-01-01','2026-12-31');
SELECT * FROM v_r2_distribucion_especies ORDER BY ejemplares DESC LIMIT 30;
SELECT * FROM v_r3_visitantes_evaluacion ORDER BY participantes DESC LIMIT 30;
CALL sp_r4_parques_excursiones('2026-01-01','2026-12-31');
SELECT * FROM v_r5_asistencia_area ORDER BY tasaAsistencia DESC LIMIT 30;
SELECT * FROM v_r6_especies_mayor_inventario ORDER BY totalInventariado DESC LIMIT 30;
SELECT * FROM v_r7_proyectos_investigacion ORDER BY investigadores DESC LIMIT 30;
SELECT * FROM v_r8_trabajadores_multifuncion ORDER BY totalFunciones DESC LIMIT 30;
CALL sp_r9_excursiones_sobre_promedio(1,'2026-01-01','2026-12-31');
CALL sp_r10_especies_sobre_promedio('Vegetal');
CALL sp_r11_visitantes_destacados('2026-01-01','2026-12-31');
CALL sp_r12_parques_sobre_promedio('2026-01-01','2026-12-31');
