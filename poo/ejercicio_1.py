class Vehiculo:
    new_id = 1

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.id = Vehiculo.new_id

    def get_id(self):
        return f"El id del vehículo es: {self.id}"


if __name__ == "__main__":
    vehiculo = Vehiculo("Toyota", "Corolla")
    print(vehiculo.get_id())
