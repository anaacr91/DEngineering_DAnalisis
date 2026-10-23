

def contenido_por_tipo(df):
    """
    TODO:
    - Analizar la columna que indica el tipo de contenido
    - Calcular cuantos titulos hay de cada tipo (por ejemplo Movie y TV Show)
    - Devolver el resultado en una estructura adecuada para su posterior analisis o visualizacion
    """
    conteo = df['type'].value_counts()
    
    print("\n--- Contenido por tipo ---")
    print(conteo)
    
    return conteo


def contenido_por_anio(df):
    """
    TODO:
    - Analizar la columna de anio de lanzamiento
    - Calcular cuantos titulos se publicaron en cada anio
    - Ordenar el resultado de forma cronologica
    - Devolver el resultado
    """
    conteo = df['release_year'].value_counts().sort_index()
    
    print("\n--- Contenido por año (primeros 10 años) ---")
    print(conteo.head(10))
    
    return conteo


def top_paises(df, n=5):
    """
    TODO:
    - Analizar la columna de pais
    - Calcular que paises tienen mayor numero de titulos
    - Devolver unicamente los n paises con mas contenido
    """

    conteo = df['country'].value_counts().head(n)
    
    print(f"\n--- Top {n} países con más contenido ---")
    print(conteo)
    
    return conteo


def top_generos(df, n=5):
    """
    TODO:
    - Analizar la columna de generos, teniendo en cuenta que puede haber varios generos por titulo
    - Separar correctamente los distintos generos
    - Calcular cuantos titulos hay por genero
    - Devolver unicamente los n generos mas frecuentes
    """

    generos_separados = df['listed_in'].str.split(', ').explode()
    
    conteo = generos_separados.value_counts().head(n)
    
    print(f"\n--- Top {n} géneros más frecuentes ---")
    print(conteo)
    
    return conteo


def contenido_por_rating(df):
    """
    TODO:
    - Analizar la columna de rating
    - Calcular cuantos titulos hay por cada rating
    - Tener en cuenta valores faltantes o inconsistentes
    - Devolver el resultado
    """
    conteo = df['rating'].value_counts(dropna=False)
    
    print("\n--- Contenido por rating ---")
    print(conteo)
    
    nulos = df['rating'].isnull().sum()
    if nulos > 0:
        print(f"\nValores nulos encontrados: {nulos}")
    
    return conteo
