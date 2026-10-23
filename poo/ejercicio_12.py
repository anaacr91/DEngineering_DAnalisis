class Cuadros:
    def __init__(self, precio, autor, antiguedad):
        self.precio = precio
        self.autor = autor
        self.antiguedad = antiguedad

    def __repr__(self):
        return f"{self.precio}, {self.autor}, {self.antiguedad}"


class Compra:
    def __init__(self):
        self.galeria = []

    def __add__(self, cuadro):
        if not isinstance(cuadro, Cuadros):
            raise TypeError("Solo se pueden añadir instancias de Cuadros.")
        self.galeria.append(cuadro)
        return self

    def __repr__(self):
        return ", ".join(repr(cuadro) for cuadro in self.galeria)
