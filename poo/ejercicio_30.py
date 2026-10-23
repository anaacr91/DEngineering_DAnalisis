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

    def es_igual(self, n):
        n = n if isinstance(n, Natural) else Natural(n)
        return self.valor == n.valor

    def es_mayor(self, n):
        n = n if isinstance(n, Natural) else Natural(n)
        actual = Natural(self.valor)
        otro = Natural(n.valor)
        while not actual.es_igual(otro) and otro.valor > 0:
            actual = actual.get_next()
            otro = Natural(otro.valor - 1)
        if otro.valor == 0 and actual.valor > 0:
            return True
        return False


class Entero(Natural):
    def __init__(self, signo, valor):
        super().__init__(abs(valor))
        self.signo = "-" if signo == "-" and self.valor != 0 else "+"

    def __repr__(self):
        return f"-{self.valor}" if self.signo == "-" else str(self.valor)

    def sumar(self, otro):
        if not isinstance(otro, Entero):
            raise TypeError("Se debe sumar otro Entero.")
        if self.signo == otro.signo:
            resultado = super().sumar(Natural(otro.valor))
            return Entero(self.signo, resultado.valor)
        if self.valor == otro.valor:
            return Entero("+", 0)
        if self.es_mayor(otro):
            diferencia = self.valor
            contador = 0
            while contador < otro.valor:
                diferencia -= 1
                contador += 1
            return Entero(self.signo, diferencia)
        diferencia = otro.valor - self.valor
        return Entero(otro.signo, diferencia)

    def restar(self, otro):
        signo_opuesto = "+" if otro.signo == "-" else "-"
        return self.sumar(Entero(signo_opuesto, otro.valor))

    def es_igual(self, z):
        return isinstance(z, Entero) and self.signo == z.signo and self.valor == z.valor

    def es_mayor(self, z):
        if not isinstance(z, Entero):
            raise TypeError("Se debe comparar con otro Entero.")
        if self.signo != z.signo:
            return self.signo == "+"
        if self.signo == "+":
            return super().es_mayor(Natural(z.valor))
        return z.valor > self.valor
