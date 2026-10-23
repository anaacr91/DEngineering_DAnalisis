import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("sample_mflix.movies.csv")

# Asegurar tipos correctos
df["_id"] = pd.to_numeric(df["_id"], errors="coerce")
df["total_movies"] = pd.to_numeric(df["total_movies"], errors="coerce")

# Quitar filas con NaN (por si acaso)
df = df.dropna()

# Ordenar por año
df = df.sort_values("_id")

# Crear gráfico
plt.figure(figsize=(10, 5))
plt.bar(df["_id"].astype(int), df["total_movies"])
plt.xlabel("Año")
plt.ylabel("Número de películas")
plt.title("Número de películas por año")
plt.tight_layout()
plt.show()
