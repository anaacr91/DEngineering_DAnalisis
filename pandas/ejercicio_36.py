edad_mas_frecuente_supervivientes = titanic.loc[titanic["survived"] == 1, "age"].mode().iloc[0]
