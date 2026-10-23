import pandas as pd


def cargar_dataset(ruta_csv= "netflix_titles.csv"):
    """
    TODO:
    - Cargar el archivo CSV indicado por la ruta recibida como parametro
    - Comprobar que el archivo se ha cargado correctamente
    - Devolver el DataFrame resultante
    """
    try:
       
        df = pd.read_csv(ruta_csv)

        print(f"Dataset cargado correctamente desde: {ruta_csv}")
        print(f"Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")
        
        return df
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {ruta_csv}")
        return None
    except Exception as e:
        print(f"Error al cargar el dataset: {e}")
        return None


def exploracion_inicial(df):
    """
    TODO:
    - Mostrar las primeras filas del dataset para entender su estructura
    - Mostrar el numero de filas y columnas
    - Mostrar los tipos de datos de cada columna
    - Mostrar el numero de valores nulos por columna
    - Usar esta informacion para detectar posibles problemas de calidad de datos
    """
    print("=" * 80)
    print("EXPLORACIÓN INICIAL DEL DATASET")
    print("=" * 80)
    
    print("\n--- Primeras 5 filas ---")
    print(df.head())
    
    print(f"\n--- Dimensiones del dataset ---")
    print(f"Número de filas: {df.shape[0]}")
    print(f"Número de columnas: {df.shape[1]}")
    
    print("\n--- Tipos de datos ---")
    print(df.dtypes)
    
    print("\n--- Información general ---")
    print(df.info())
    
    print("\n--- Valores nulos por columna ---")
    valores_nulos = df.isnull().sum()
    porcentaje_nulos = (valores_nulos / len(df)) * 100
    
    resumen_nulos = pd.DataFrame({
        'Valores Nulos': valores_nulos,
        'Porcentaje (%)': porcentaje_nulos
    })
    
    resumen_nulos_filtrado = resumen_nulos[resumen_nulos['Valores Nulos'] > 0]
    
    if len(resumen_nulos_filtrado) > 0:
        print(resumen_nulos_filtrado)
    else:
        print("No hay valores nulos en el dataset")
    
    print("\n" + "=" * 80)
