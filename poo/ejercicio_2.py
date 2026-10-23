class Vehiculo:
    new_id = 1

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.id = Vehiculo.new_id
        Vehiculo.new_id += 1

    def get_id(self):
        return f"El id del vehículo es: {self.id}"


if __name__ == "__main__":
    print(Vehiculo("Toyota", "Corolla").get_id())
    print(Vehiculo("Seat", "Ibiza").get_id())
