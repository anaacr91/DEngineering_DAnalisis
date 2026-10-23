class Vehiculo:
    new_id = 1

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.id = Vehiculo.new_id
        Vehiculo.new_id += 1

    def get_id(self):
        return f"El id del vehículo es: {self.id}"

    def __repr__(self):
        return (f"Vehiculo(marca={self.marca!r}, modelo={self.modelo!r}, "
                f"id={self.id})")


class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas


if __name__ == "__main__":
    print(Coche("Seat", "Ibiza", 5))
