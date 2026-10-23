edad_media_mujeres_supervivientes = titanic.loc[(titanic["sex"] == "female") & (titanic["survived"] == 1)].groupby("pclass")["age"].mean()
