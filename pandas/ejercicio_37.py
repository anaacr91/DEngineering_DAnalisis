import pandas as pd

data = {
    "nombre": ["Ana", "Luis", "Carlos", "Sofía", "Miguel"],
    "salario": [2500, 3000, 4000, 2800, 3500],
    "experiencia": [2, 5, 10, 3, 7],
}
df = pd.DataFrame(data)

def calcular_bono(fila):
    if fila["experiencia"] < 3:
        porcentaje = 0.05
    elif fila["experiencia"] <= 7:
        porcentaje = 0.10
    else:
        porcentaje = 0.15
    return fila["salario"] * porcentaje

df["bono"] = df.apply(calcular_bono, axis=1)
print(df)
