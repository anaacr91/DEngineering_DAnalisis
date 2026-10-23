# Fundamentos de R - Ejercicio entregable 

ruta_csv<- file.choose()
# 1. Carga del dataset
cargar_dataset <- function(ruta_csv) {
  # TODO:
  # - Leer el archivo CSV indicado por ruta_csv
  # - Asegurarse de que las cadenas no se convierten en factores
  # - Devolver el dataset como data.frame
  if (!is.character(ruta_csv) || length(ruta_csv) != 1) {
    stop("La ruta del CSV debe ser una cadena (character) de longitud 1.")
  }
  if (!file.exists(ruta_csv)) {
    stop(paste("No existe el archivo:", ruta_csv))
  }
  
  df <- read.csv(ruta_csv, stringsAsFactors = FALSE)
  return(df)
}




# 2. Validacion de estructura
validar_estructura <- function(df) {
  # TODO:
  # - Comprobar que df es un data.frame
  # - Definir un vector con las columnas esperadas:
  #   "id", "edad", "nota", "asistencia"
  # - Comprobar que todas las columnas existen en el dataset
  # - Devolver TRUE si la estructura es correcta
  # - Devolver FALSE en caso contrario
  if (!is.data.frame(df)) return(FALSE)
  
  columnas_esperadas <- c("id", "edad", "nota", "asistencia")
  existen <- columnas_esperadas %in% names(df)
  
  if (!all(existen)) return(FALSE)
  return(TRUE)
}


# 3. Limpieza de datos
limpiar_dataset <- function(df) {
  # TODO:
  # - Eliminar las filas con valores NA en la columna "nota"
  # - Eliminar las filas con valores NA en la columna "asistencia"
  # - Devolver el data.frame limpio
  if (!("nota" %in% names(df)) || !("asistencia" %in% names(df))) {
    return(df)
  }
  
  df_limpio <- df[!is.na(df$nota) & !is.na(df$asistencia), , drop = FALSE]
  rownames(df_limpio) <- NULL
  
  return(df_limpio)
}



# 4. Validacion de valores
validar_valores <- function(df) {
  # TODO:
  # - Comprobar que todas las notas estan entre 0 y 10
  # - Comprobar que todas las asistencias estan entre 0 y 1
  # - Si algun valor no cumple las condiciones, devolver FALSE
  # - Si todo es correcto, devolver TRUE
  notas_ok <- all(df$nota[!is.na(df$nota)] >= 0 & df$nota[!is.na(df$nota)] <= 10)
  asis_ok  <- all(df$asistencia[!is.na(df$asistencia)] >= 0 & df$asistencia[!is.na(df$asistencia)] <= 1)
  
  if (!notas_ok || !asis_ok) return(FALSE)
  return(TRUE)
}



# 5. Clasificacion de notas
clasificar_nota <- function(nota) {
  # TODO:
  # - Si nota < 5 devolver "Suspenso"
  # - Si nota >= 5 y < 7 devolver "Aprobado"
  # - Si nota >= 7 y < 9 devolver "Notable"
  # - Si nota >= 9 devolver "Sobresaliente"
  # - Devolver siempre una cadena de texto
  if (is.na(nota)) return(NA_character_)
  
  if (nota < 5) {
    return("Suspenso")
  } else if (nota >= 5 && nota < 7) {
    return("Aprobado")
  } else if (nota >= 7 && nota < 9) {
    return("Notable")
  } else {
    return("Sobresaliente")
  }
}




# 6. Agregar clasificacion
agregar_clasificacion <- function(df) {
  # TODO:
  # - Crear una nueva columna llamada "categoria"
  # - Aplicar la funcion clasificar_nota a cada valor de la columna "nota"
  # - Devolver el data.frame actualizado
  categorias <- character(nrow(df))
  
  for (i in seq_len(nrow(df))) {
    categorias[i] <- clasificar_nota(df$nota[i])
  }
  
  df$categoria <- categorias
  return(df)
}




# 7. Estadisticas basicas
estadisticas_basicas <- function(vector) {
  # TODO:
  # - Calcular la media del vector
  # - Calcular el valor minimo del vector
  # - Calcular el valor maximo del vector
  # - Devolver una lista con los tres valores
  v <- vector[!is.na(vector)]
  
  if (length(v) == 0) {
    return(list(media = NA_real_, minimo = NA_real_, maximo = NA_real_))
  }
  
  media_val <- mean(v)
  min_val <- min(v)
  max_val <- max(v)
  
  return(list(media = media_val, minimo = min_val, maximo = max_val))
}




# 8. Estadisticas por categoria
estadisticas_por_categoria <- function(df) {
  # TODO:
  # - Obtener las categorias unicas del dataset
  # - Crear una lista vacia para almacenar los resultados
  # - Para cada categoria:
  #     * Filtrar las notas correspondientes
  #     * Calcular estadisticas_basicas
  #     * Guardar el resultado en la lista usando el nombre de la categoria
  # - Devolver la lista final
  categorias <- unique(df$categoria)
  resultados <- list()
  
  for (cat in categorias) {
    notas_cat <- df$nota[df$categoria == cat]
    resultados[[cat]] <- estadisticas_basicas(notas_cat)
  }
  
  return(resultados)
}




# 9. Ranking de estudiantes
ranking_estudiantes <- function(df, top_n = 5) {
  # TODO:
  # - Ordenar el data.frame de forma descendente por la columna "nota"
  # - Devolver los top_n primeros estudiantes
  if (!is.numeric(top_n) || length(top_n) != 1 || top_n <= 0) {
    top_n <- 5
  }
  top_n <- as.integer(top_n)
  
  orden <- order(df$nota, decreasing = TRUE, na.last = TRUE)
  df_ord <- df[orden, , drop = FALSE]
  
  n <- min(top_n, nrow(df_ord))
  return(df_ord[seq_len(n), , drop = FALSE])
  }





# 10. Tramos de edad
clasificar_edad <- function(edad) {
  # TODO:
  # - Si edad < 20 devolver "Menores de 20"
  # - Si edad esta entre 20 y 22 (inclusive) devolver "20 a 22"
  # - Si edad > 22 devolver "Mayores de 22"
  if (is.na(edad)) return(NA_character_)
  
  if (edad < 20) {
    return("Menores de 20")
  } else if (edad >= 20 && edad <= 22) {
    return("20 a 22")
  } else {
    return("Mayores de 22")
  }
}




# 11. Analisis por edad
analisis_por_edad <- function(df) {
  # TODO:
  # - Crear una nueva columna "tramo_edad" usando clasificar_edad
  # - Obtener los tramos de edad unicos
  # - Para cada tramo:
  #     * Filtrar las notas correspondientes
  #     * Calcular estadisticas_basicas
  #     * Guardar el resultado en una lista
  # - Devolver la lista final
  tramos <- character(nrow(df))
  
  for (i in seq_len(nrow(df))) {
    tramos[i] <- clasificar_edad(df$edad[i])
  }
  
  df$tramo_edad <- tramos
  
  tramos_unicos <- unique(df$tramo_edad)
  resultados <- list()
  
  for (t in tramos_unicos) {
    notas_t <- df$nota[df$tramo_edad == t]
    resultados[[t]] <- estadisticas_basicas(notas_t)
  }
  
  return(resultados)
  
}




# 12. Resumen final complejo
resumen_final <- function(df) {
  # TODO:
  # - Crear una lista que contenga:
  #     * resumen_general:
  #         - numero total de estudiantes
  #         - estadisticas basicas de la nota
  #     * por_categoria:
  #         - resultado de estadisticas_por_categoria
  #     * por_edad:
  #         - resultado de analisis_por_edad
  #     * ranking:
  #         - resultado de ranking_estudiantes
  #     * baja_asistencia:
  #         - estudiantes con asistencia menor a 0.75
  # - Devolver la lista completa
  resumen_general <- list(
    total_estudiantes = nrow(df),
    estadisticas_nota = estadisticas_basicas(df$nota)
  )
  
  por_categoria <- estadisticas_por_categoria(df)
  
  por_edad <- analisis_por_edad(df)
  
  ranking <- ranking_estudiantes(df, top_n = 5)
  
  baja_asistencia <- df[df$asistencia < 0.75, , drop = FALSE]
  rownames(baja_asistencia) <- NULL
  
  resultado <- list(
    resumen_general = resumen_general,
    por_categoria = por_categoria,
    por_edad = por_edad,
    ranking = ranking,
    baja_asistencia = baja_asistencia
  )
  
  return(resultado)
}




# 13. Funcion principal
main <- function() {
  # TODO:
  # - Definir la ruta al archivo CSV
  # - Cargar el dataset
  # - Validar la estructura del dataset
  # - Si la estructura no es valida:
  #     * Mostrar un mensaje de error
  #     * Detener la ejecucion
  # - Limpiar el dataset
  # - Validar los valores del dataset
  # - Si los valores no son validos:
  #     * Mostrar un mensaje de error
  #     * Detener la ejecucion
  # - Agregar la clasificacion de notas
  # - Generar el resumen final
  # - Mostrar los resultados por consola
  ruta_csv <- file.choose()
  cat("== Cargando dataset ==\n")
  df <- cargar_dataset(ruta_csv)
  
  cat("== Validando estructura ==\n")
  if (!validar_estructura(df)) {
    cat("ERROR: Estructura inválida. Debe incluir columnas: id, edad, nota, asistencia.\n")
    stop("Ejecución detenida por estructura inválida.")
  }
  
  cat("== Limpiando dataset ==\n")
  df <- limpiar_dataset(df)
  
  cat("== Validando valores ==\n")
  if (!validar_valores(df)) {
    cat("ERROR: Valores inválidos. Nota debe estar entre 0-10 y asistencia entre 0-1.\n")
    stop("Ejecución detenida por valores inválidos.")
  }
  
  cat("== Agregando clasificación de notas ==\n")
  df <- agregar_clasificacion(df)
  
  cat("== Generando resumen final ==\n")
  res <- resumen_final(df)
  
  cat("\n================ RESULTADOS ================\n")
  cat("\n--- Resumen general ---\n")
  print(res$resumen_general)
  
  cat("\n--- Estadísticas por categoría ---\n")
  print(res$por_categoria)
  
  cat("\n--- Estadísticas por tramo de edad ---\n")
  print(res$por_edad)
  
  cat("\n--- Ranking (Top 5) ---\n")
  print(res$ranking)
  
  cat("\n--- Baja asistencia (< 0.75) ---\n")
  print(res$baja_asistencia)
  
}



# 14. Ejecucion


# TODO:
# - Llamar a la funcion main()
main()

