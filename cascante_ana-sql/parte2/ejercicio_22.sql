SELECT nombre, domicilio, edad, 'alumno' AS condicion
FROM alumnos

UNION ALL

SELECT nombre, domicilio, edad, 'profesor' AS condicion
FROM profesores;
