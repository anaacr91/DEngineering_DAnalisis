import pandas as pd

data = {
    "nombre": [" juan ", "MARÍA", "PeDro ", " ana", "luis"],
    "edad": [25, 30, 22, 28, 35],
}
df = pd.DataFrame(data)
df["nombre"] = df["nombre"].str.strip().str.lower().str.capitalize()
print(df)
