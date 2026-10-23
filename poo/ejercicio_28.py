class Natural:
    def __init__(self, valor):
        if not isinstance(valor, int) or isinstance(valor, bool):
            raise TypeError("El valor debe ser un entero.")
        if valor < 0:
            raise ValueError("Un número natural no puede ser negativo.")
        self.valor = valor

    def __repr__(self):
        return f"Natural({self.valor})"

    def get_next(self):
        return Natural(self.valor + 1)

    def sumar(self, n):
        if not isinstance(n, Natural):
            n = Natural(n)
        resultado = self
        contador = 0
        while contador < n.valor:
            resultado = resultado.get_next()
            contador += 1
        return resultado

    def multiplicar(self, n):
        if not isinstance(n, Natural):
            n = Natural(n)
        resultado = Natural(0)
        contador = 0
        while contador < n.valor:
            resultado = resultado.sumar(self)
            contador += 1
        return resultado

    def es_divisor(self, d):
        d = d if isinstance(d, Natural) else Natural(d)
        if d.valor == 0:
            raise ZeroDivisionError("Cero no puede ser divisor.")
        return self.valor % d.valor == 0

    def es_primo(self):
        if self.valor < 2:
            return False
        divisor = 2
        while divisor * divisor <= self.valor:
            if self.valor % divisor == 0:
                return False
            divisor += 1
        return True
