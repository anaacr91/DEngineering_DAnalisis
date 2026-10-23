import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample_training.companies.csv")

plt.figure(figsize=(10,5))
plt.bar(df["_id"].astype(str), df["total_companies"])
plt.xlabel("Categoría (category_code)")
plt.ylabel("Número de empresas")
plt.title("Top 10 categorías con más empresas (sample_training.companies)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
