pais_mas_supervivientes_mayores_50 = titanic.loc[(titanic["survived"] == 1) & (titanic["age"] > 50), "country"].value_counts().idxmax()
