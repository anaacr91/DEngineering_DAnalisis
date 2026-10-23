pasajero_mas_joven_canada = titanic.loc[titanic["country"] == "Canada"].sort_values("age").loc[:, ["name", "survived"]].head(1)
