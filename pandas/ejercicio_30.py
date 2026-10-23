porcentaje_supervivencia = titanic.groupby(["pclass", "Young"])["survived"].mean().mul(100).rename("porcentaje_supervivencia").reset_index()
