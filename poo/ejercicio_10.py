from datetime import date


class Vehiculo:
    new_id = 1

    def __init__(self, marca, modelo, fecha):
        self.marca = marca
        self.modelo = modelo
        self.id = Vehiculo.new_id
        Vehiculo.new_id += 1
        self.fecha = date.fromisoformat(fecha)

    def __repr__(self):
        return (f"Vehiculo(marca={self.marca!r}, modelo={self.modelo!r}, "
                f"id={self.id}, fecha={self.fecha.isoformat()!r})")


class Coche(Vehiculo):
    def __init__(self, marca, modelo, fecha, puertas):
        super().__init__(marca, modelo, fecha)
        self.puertas = puertas

    def __repr__(self):
        return f"{super().__repr__()}, puertas={self.puertas}"


class Cliente:
    def __init__(self, nombre, dni, edad, compras):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.compras = compras

    def es_vip(self):
        return self.compras > 3

    def __repr__(self):
        return (f"Cliente(nombre={self.nombre!r}, dni={self.dni!r}, "
                f"edad={self.edad}, compras={self.compras})")


class Contrato(Vehiculo, Cliente):
    new_contract_id = 1

    def __init__(self, marca, modelo, fecha, dni, precio):
        Vehiculo.__init__(self, marca, modelo, fecha)
        self.nombre = ""
        self.dni = dni
        self.edad = 0
        self.compras = 0
        self.precio = precio
        self.id_contrato = Contrato.new_contract_id
        Contrato.new_contract_id += 1


if __name__ == "__main__":
    cliente = Cliente("Ana", "12345678A", 30, 4)
    print(cliente.es_vip())
