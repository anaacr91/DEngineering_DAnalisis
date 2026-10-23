class Natural:
    def __init__(self, valor):
        if not isinstance(valor, int) or isinstance(valor, bool):
            raise TypeError("El valor debe ser un entero.")
        if valor < 0:
            raise ValueError("Un número natural no puede ser negativo.")
        self.valor = valor

    def __repr__(self):
        return f"Natural({self.valor})"
