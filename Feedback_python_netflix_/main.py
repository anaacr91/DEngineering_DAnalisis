from data_loader import *
from data_cleaning import *
from analysis import *
from visualization import *

# BONUS
# from netflix_analyzer import NetflixAnalyzer


def main():
    """
    TODO:
    - Definir la ruta al archivo netflix_titles.csv
    - Cargar el dataset usando la funcion de carga
    - Realizar una exploracion inicial del dataset para detectar posibles problemas
    - Limpiar y preparar los datos antes del analisis
    - Ejecutar las funciones de analisis definidas en el proyecto
    - Mostrar por pantalla los resultados principales del analisis
    - Generar y mostrar las visualizaciones correspondientes
    - Asegurarse de que el flujo de ejecucion sigue un orden logico
    """
    print("="*80)
    print("PROYECTO DE ANÁLISIS DE DATOS DE NETFLIX")
    print("="*80)
    
    ruta_csv = 'netflix_titles.csv'
    
    print("\n[1] CARGANDO DATASET...")
    df = cargar_dataset(ruta_csv)
    
    if df is None:
        print("Error: No se pudo cargar el dataset. Finalizando programa.")
        return
    
    print("\n[2] EXPLORACIÓN INICIAL DEL DATASET...")
    exploracion_inicial(df)
    
    print("\n[3] LIMPIEZA Y PREPARACIÓN DE DATOS...")
    df_limpio = preparar_dataset(df)
    print("Datos limpiados correctamente.")
    
    print("\n[4] ANÁLISIS DE DATOS...")
    print("\n" + "="*80)
    
    contenido_por_tipo(df_limpio)
    
    contenido_por_anio(df_limpio)
    
    top_paises(df_limpio, n=10)
    
    top_generos(df_limpio, n=10)
    
    contenido_por_rating(df_limpio)
    
    print("\n" + "="*80)
    
    print("\n[5] GENERANDO VISUALIZACIONES...")
    print("Cerrando cada gráfico para ver el siguiente...\n")
    
    grafico_contenido_por_tipo(df_limpio)
    
    grafico_contenido_por_anio(df_limpio)
    
    grafico_top_paises(df_limpio, n=10)
    
    grafico_distribucion_duracion(df_limpio)
    
    grafico_contenido_por_rating(df_limpio)
    
    grafico_top_generos(df_limpio, n=10)
    
    print("\n" + "="*80)
    print("ANÁLISIS COMPLETADO EXITOSAMENTE")
    print("="*80)


if __name__ == "__main__":
    """
    TODO:
    - Ejecutar la funcion main
    - Verificar que todo el flujo del programa se ejecuta correctamente
    """
    main()
