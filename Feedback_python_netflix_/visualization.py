import seaborn as sns
import matplotlib.pyplot as plt
from analysis import contenido_por_rating, top_generos


def grafico_contenido_por_tipo(df):
    """
    TODO:
    - Generar un grafico de barras usando seaborn
    - Comparar el numero de titulos por tipo de contenido
    - Utilizar la columna type del dataset
    - Anadir titulo y etiquetas a los ejes
    - Mostrar el grafico por pantalla
    """
    plt.figure(figsize=(8, 6))
    
    sns.countplot(data=df, x='type', palette='viridis')
    
    plt.title('Distribución de Contenido por Tipo', fontsize=16, fontweight='bold')
    plt.xlabel('Tipo de Contenido', fontsize=12)
    plt.ylabel('Número de Títulos', fontsize=12)
    
    plt.tight_layout()
    plt.show()


def grafico_contenido_por_anio(df):
    """
    TODO:
    - Generar un grafico de lineas usando seaborn
    - Representar la evolucion del numero de titulos por anio de lanzamiento
    - Asegurarse de que los datos estan ordenados cronologicamente
    - Anadir titulo y etiquetas a los ejes
    - Mostrar el grafico por pantalla
    """
    plt.figure(figsize=(12, 6))
    
    contenido_anio = df['release_year'].value_counts().sort_index()
    
    sns.lineplot(x=contenido_anio.index, y=contenido_anio.values, marker='o', linewidth=2)
    
    plt.title('Evolución de Contenido por Año', fontsize=16, fontweight='bold')
    plt.xlabel('Año de Lanzamiento', fontsize=12)
    plt.ylabel('Número de Títulos', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()


def grafico_top_paises(df, n=5):
    """
    TODO:
    - Generar un grafico de barras usando seaborn
    - Mostrar los n paises con mayor numero de titulos
    - Utilizar la columna country del dataset
    - Anadir titulo y etiquetas a los ejes
    - Mostrar el grafico por pantalla
    """
    plt.figure(figsize=(10, 6))
    
    top_paises_data = df['country'].value_counts().head(n)
    
    sns.barplot(x=top_paises_data.values, y=top_paises_data.index, palette='rocket')
    
    plt.title(f'Top {n} Países con Más Contenido', fontsize=16, fontweight='bold')
    plt.xlabel('Número de Títulos', fontsize=12)
    plt.ylabel('País', fontsize=12)
    
    plt.tight_layout()
    plt.show()


def grafico_distribucion_duracion(df):
    """
    TODO:
    - Analizar la columna duration_num
    - Eliminar valores nulos antes de generar el grafico
    - Crear un histograma de la distribucion de duracion
    - Diferenciar el tipo de contenido usando colores
    - Anadir titulo y etiquetas a los ejes
    - Mostrar el grafico por pantalla
    """
    plt.figure(figsize=(12, 6))
    
    df_limpio = df.dropna(subset=['duration_num'])
    
    sns.histplot(data=df_limpio, x='duration_num', hue='type', kde=True, bins=30, palette='Set2')
    
    plt.title('Distribución de Duración por Tipo de Contenido', fontsize=16, fontweight='bold')
    plt.xlabel('Duración (Minutos para Movies / Temporadas para TV Shows)', fontsize=12)
    plt.ylabel('Frecuencia', fontsize=12)
    plt.legend(title='Tipo')
    
    plt.tight_layout()
    plt.show()


def grafico_contenido_por_rating(df):
    """
    TODO:
    - Analizar la columna rating
    - Calcular el numero de titulos por tipo de rating
    - Generar un grafico de barras usando seaborn
    - Rotar las etiquetas si es necesario para mejorar la lectura
    - Anadir titulo y etiquetas a los ejes
    - Mostrar el grafico por pantalla
    """
    plt.figure(figsize=(12, 6))
    
    conteo_rating = contenido_por_rating(df)
    
    sns.barplot(x=conteo_rating.index, y=conteo_rating.values, palette='mako')
    
    plt.title('Distribución de Contenido por Rating', fontsize=16, fontweight='bold')
    plt.xlabel('Rating', fontsize=12)
    plt.ylabel('Número de Títulos', fontsize=12)
    
    plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    plt.show()


def grafico_top_generos(df, n=5):
    """
    TODO:
    - Analizar la columna listed_in para obtener los generos
    - Calcular los n generos mas frecuentes
    - Generar un grafico de barras usando seaborn
    - Anadir titulo y etiquetas a los ejes
    - Mostrar el grafico por pantalla
    """
    plt.figure(figsize=(10, 6))
    
    top_generos_data = top_generos(df, n)
    
    sns.barplot(x=top_generos_data.values, y=top_generos_data.index, palette='coolwarm')
    
    plt.title(f'Top {n} Géneros Más Frecuentes', fontsize=16, fontweight='bold')
    plt.xlabel('Número de Títulos', fontsize=12)
    plt.ylabel('Género', fontsize=12)
    
    plt.tight_layout()
    plt.show()
