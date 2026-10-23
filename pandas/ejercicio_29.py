titanic = titanic.dropna(subset=["age"]).copy()
titanic["Young"] = titanic["age"] < 18
