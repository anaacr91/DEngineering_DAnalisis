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

    def __len__(self):
        return len(self.galeria)

    def total_price(self):
        total = sum(cuadro.precio for cuadro in self.galeria)
        return total * 0.9 if len(self.galeria) > 10 else total


if __name__ == "__main__":
    cuadro1 = Cuadros(5000, "Picasso", 80)
    cuadro2 = Cuadros(3000, "Van Gogh", 130)
    cuadro3 = Cuadros(70000, "Picasso", 82)
    compra1 = Compra()
    compra1 + cuadro1
    compra1 + cuadro2
    compra1 + cuadro3
    print(compra1)
    print("Número de cuadros:", len(compra1))
    print("Precio total:", compra1.total_price())
