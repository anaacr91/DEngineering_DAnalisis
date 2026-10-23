<<<<<<< HEAD
## Plantilla Bash
Para la realización de esta tarea, debes trabajar con tecnología Bash.

Dentro de Bash, debes entrar en el subbloque comandos y, dentro de tu carpeta de alumno, crear un archivo por cada ejercicio.
=======
# Plantilla alumno_base
Repositorio estandar para replicar

# Plantilla final de entrega por subbloque
Cada alumno trabaja con un único repositorio. La estructura final debe seguir siempre este orden:
>>>>>>> parent of 39f4794 (Merge pull request #2 from primera-edicion-bigdata-ia/sql)

1. apellido_nombre
2. bloque
3. subbloque
4. ejercicio_N.ext

<<<<<<< HEAD
1. Subir tu trabajo a tu repositorio en la rama `bash`.
2. Guardar tu entrega dentro de la estructura: `apellido_nombre/bash/comandos/`. Mirar readme de main como ejemplo.
 
Siendo:
- apellido_nombre nuestro repo
- bash la rama
- comandos la carpeta donde irán los ejercicios

3. Nombrar los archivos con el patrón:
- `ejercicio_1.sh`, `ejercicio_2.sh`, ..., `ejercicio_N.sh`.
- También se admite `ejercicio_N.txt` cuando el ejercicio sea solo línea de comando.
4. Exportar tu entrega en un archivo zip con la nomenclatura:
- `Bash - Ejercicios - Apellido_Nombre.zip`.
5. Subir ese zip a la plataforma L2E.
=======
Objetivo: que el docente pueda clonar el repositorio, entrar en la ruta correcta y corregir con el agente sin ambigüedades.

## Regla principal de entrega
El alumno solo sube sus ejercicios dentro del subbloque que se esté trabajando.

## Rama por bloque
1. Si el bloque activo es Bash, trabajar y subir en la rama bash.
2. Si el bloque activo es SQL, trabajar y subir en la rama sql.
3. Si el bloque activo es Python, trabajar y subir en la rama python.
4. Si el bloque activo es Spark, trabajar y subir en la rama spark.

## Estructura final del repositorio
La estructura general del repositoria debe ser:
- apellido_nombre/bloque/subbloque/ejercicio_N.ext

Siendo:
- apellido_nombre nuestro repo
- bloque la rama
- subbloque la carpeta que crearemos según el tipo de ejercicio

## Estructura por bloque
### Bash

- apellido_nombre/bash/comandos/ejercicio_1.txt
- apellido_nombre/bash/comandos/ejercicio_2.txt
- apellido_nombre/bash/comandos/ejercicio_N.txt

### SQL
- apellido_nombre/sql/parte1/ejercicio_1.sql
- apellido_nombre/sql/parte1/ejercicio_2.sql
- apellido_nombre/sql/parte1/ejercicio_N.md (si el ejercicio es conceptual)

- apellido_nombre/sql/parte2/ejercicio_1.sql
- apellido_nombre/sql/parte2/ejercicio_2.sql
- apellido_nombre/sql/parte2/ejercicio_N.md (si el ejercicio es conceptual)

- apellido_nombre/sql/parte3/ejercicio_1.sql
- apellido_nombre/sql/parte3/ejercicio_2.sql
- apellido_nombre/sql/parte3/ejercicio_N.md (si el ejercicio es conceptual)

### Python
- apellido_nombre/python/excepciones/ejercicio_1.py
- apellido_nombre/python/excepciones/ejercicio_2.py
- apellido_nombre/python/excepciones/ejercicio_N.md (si el ejercicio es conceptual)

- apellido_nombre/python/pandas/ejercicio_1.py
- apellido_nombre/python/pandas/ejercicio_2.py
- apellido_nombre/python/pandas/ejercicio_N.md (si el ejercicio es conceptual)

- apellido_nombre/python/POO/ejercicio_1.py
- apellido_nombre/python/POO/ejercicio_2.py
- apellido_nombre/python/POO/ejercicio_N.md (si el ejercicio es conceptual)

### Spark
- apellido_nombre/spark/RDD/ejercicio_1.py
- apellido_nombre/spark/RDD/ejercicio_2.py
- apellido_nombre/spark/RDD/ejercicio_N.md (si el ejercicio es conceptual)

- apellido_nombre/spark/DF/ejercicio_1.py
- apellido_nombre/spark/DF/ejercicio_2.py
- apellido_nombre/spark/DF/ejercicio_N.md (si el ejercicio es conceptual)

- apellido_nombre/spark/optimizacion/ejercicio_1.py
- apellido_nombre/spark/optimizacion/ejercicio_2.py
- apellido_nombre/spark/optimizacion/ejercicio_N.md (si el ejercicio es conceptual)


## Nomenclatura obligatoria
1. El subbloque, carpeta.
2. Archivos: ejercicio_N.ext.
3. Un archivo por ejercicio.
4. No mezclar extensiones para el mismo ejercicio.
5. En Bash:
   - usar .txt cuando el ejercicio sea solo línea de comando;
   - usar .sh cuando el ejercicio requiera script.

## Exportación y entrega en plataforma
1. Además del push a Git, exportar solo la carpeta del subbloque activo a un ZIP.
2. Nombre del ZIP: Bloque - Ejercicios Subbloque - Apellido_Nombre.zip.
3. Subir ese ZIP a la plataforma L2E.

Ejemplos de ZIP:
- Bash - Ejercicios Comandos - Martinez_Juan.zip
- SQL - Ejercicios Parte II - Martinez_Juan.zip
- Python - Ejercicios Excepciones - Martinez_Juan.zip
- Spark - Ejercicios RDD - Martinez_Juan.zip

## Qué no se debe subir
1. Enunciados.
2. Archivos con nombres distintos a ejercicio_N.ext para la entrega principal.
3. Archivos de otros subbloques en la entrega del subbloque activo.

## Checklist del alumno (obligatorio antes de entregar)
1. Estoy en la rama correcta del bloque.
2. He subido solo mi carpeta dentro del subbloque activo.
3. He usado la nomenclatura ejercicio_N.ext.
4. He hecho push al repositorio.
5. He subido a L2E el ZIP con nombre correcto.
>>>>>>> parent of 39f4794 (Merge pull request #2 from primera-edicion-bigdata-ia/sql)
