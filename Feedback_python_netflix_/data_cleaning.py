import numpy as np
import pandas as pd


def limpiar_columna_country(df):
    """
    TODO:
    - Analizar la columna country
    - Rellenar los valores nulos con el valor knowing 'Unknown'
    - En los casos donde haya varios paises separados por coma, quedarse solo con el primero
    - No modificar el DataFrame original
    - Devolver un nuevo DataFrame con la columna country limpia
    """
    df_limpio = df.copy()
    
    df_limpio['country'] = df_limpio['country'].fillna('Unknown')
    
    df_limpio['country'] = df_limpio['country'].apply(lambda x: x.split(',')[0].strip())
    
    return df_limpio


def extraer_duracion_numerica(row):
    """
    TODO:
    - Recibir una fila del DataFrame
    - Analizar la columna duration
    - Extraer el valor numerico de la duracion
    - Para peliculas, interpretar el valor como minutos
    - Para series, interpretar el valor como numero de temporadas
    - Devolver un entero o NaN si no es posible obtener el valor
    """
    try:
        duration = str(row['duration'])
        content_type = row['type']
        
        if pd.isna(duration) or duration == 'nan' or duration == '':
            return np.nan
        
        numero = duration.split()[0]
        valor_numerico = int(numero)
        
        if content_type == 'Movie':
            print(f"Tipo: {content_type} - Duración: {valor_numerico} minutos")
            return valor_numerico
        elif content_type == 'TV Show':
            print(f"Tipo: {content_type} - Duración: {valor_numerico} temporadas")
            return valor_numerico
        else:
            print(f"Tipo: {content_type} - Duración: {valor_numerico}")
            return valor_numerico
            
    except (ValueError, IndexError, AttributeError, KeyError):
        return np.nan


def limpiar_duracion(df):
    """
    TODO:
    - Crear una nueva columna llamada duration_num
    - Usar una funcion que procese fila a fila la columna duration
    - No modificar el DataFrame original
    - Devolver un nuevo DataFrame con la duracion numerica
    """
    df_limpio = df.copy()
    
    df_limpio['duration_num'] = df_limpio.apply(extraer_duracion_numerica, axis=1)
    
    return df_limpio


def preparar_dataset(df):
    """
    TODO:
    - Aplicar todas las funciones de limpieza necesarias sobre el dataset
    - Garantizar que el DataFrame resultante es una copia del original
    - Devolver el DataFrame final preparado para el analisis
    """
    df_preparado = df.copy()
    
    df_preparado = limpiar_columna_country(df_preparado)
    
    df_preparado = limpiar_duracion(df_preparado)
    
    return df_preparado
