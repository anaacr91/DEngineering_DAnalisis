import pandas as pd

def estadistica_notas(notas):
    serie = pd.Series(notas, dtype="float64")
    estadisticas = serie.describe(percentiles=[0.25, 0.5, 0.75])
    return estadisticas.loc[["25%", "50%", "75%", "max", "min", "mean", "std"]]

notas = {"Juan": 9, "María": 6.5, "Pedro": 4, "Carmen": 8.5, "Luis": 5}
print(estadistica_notas(notas))
