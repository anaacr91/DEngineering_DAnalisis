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


if __name__ == "__main__":
    cuadro1 = Cuadros(5000, "Picasso", 80)
    cuadro2 = Cuadros(3000, "Van Gogh", 130)
    cuadro3 = Cuadros(70000, "Picasso", 82)
    compra1 = Compra()
    compra1 + cuadro1
    compra1 + cuadro2
    compra1 + cuadro3
    print(compra1)
