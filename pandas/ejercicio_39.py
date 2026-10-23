df["iniciales"] = df["nombre"].str.strip().str.split().apply(lambda partes: "".join(p[0].upper() for p in partes if p))
