from datetime import date


class Vehiculo:
    new_id = 1

    def __init__(self, marca, modelo, fecha):
        self.marca = marca
        self.modelo = modelo
        self.id = Vehiculo.new_id
        Vehiculo.new_id += 1
        self.fecha = date.fromisoformat(fecha)

    def get_id(self):
        return f"El id del vehículo es: {self.id}"

    def get_anio(self):
        return self.fecha.year

    def get_mes(self):
        return self.fecha.month

    def get_dia(self):
        return self.fecha.day

    def __repr__(self):
        return (f"Vehiculo(marca={self.marca!r}, modelo={self.modelo!r}, "
                f"id={self.id}, fecha={self.fecha.isoformat()!r})")


class Coche(Vehiculo):
    def __init__(self, marca, modelo, fecha, puertas):
        super().__init__(marca, modelo, fecha)
        self.puertas = puertas

    def __repr__(self):
        return f"{super().__repr__()}, puertas={self.puertas}"


if __name__ == "__main__":
    v = Vehiculo("Toyota", "Corolla", "2020-05-10")
    print(v.get_anio(), v.get_mes(), v.get_dia())
