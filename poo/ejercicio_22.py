from abc import ABC, abstractmethod


class Matriz(ABC):
    def __init__(self, n, m, valores=None):
        self.n = n
        self.m = m
        self.valores = valores if valores is not None else [[0 for _ in range(m)] for _ in range(n)]

    @abstractmethod
    def dim(self):
        pass

    def sumar(self, otra):
        if not isinstance(otra, Matriz):
            raise TypeError("Solo se pueden sumar objetos de tipo Matriz.")
        if self.n != otra.n or self.m != otra.m:
            raise ValueError("Las matrices deben tener las mismas dimensiones.")
        valores = [[self.valores[i][j] + otra.valores[i][j]
                    for j in range(self.m)] for i in range(self.n)]
        return MatrizConcreta(self.n, self.m, valores)


class MatrizConcreta(Matriz):
    def dim(self):
        return self.n, self.m


class Vector(Matriz):
    def __init__(self, valores):
        super().__init__(1, len(valores), [list(valores)])

    def dim(self):
        return self.m

    def __str__(self):
        return "(" + ",".join(map(str, self.valores[0])) + ")"

    def sumar(self, otro):
        if not isinstance(otro, Matriz):
            raise TypeError("Solo se pueden sumar objetos de tipo Matriz.")
        if not isinstance(otro, Vector):
            raise TypeError("Para sumar un Vector, el otro objeto también debe ser Vector.")
        if self.m != otro.m:
            raise ValueError("Los vectores deben tener la misma dimensión.")
        return Vector([a + b for a, b in zip(self.valores[0], otro.valores[0])])

    def prod_escalar(self, otro):
        if not isinstance(otro, Vector):
            raise TypeError("El producto escalar requiere otro Vector.")
        if self.m != otro.m:
            raise ValueError("Los vectores deben tener la misma dimensión.")
        return sum(a * b for a, b in zip(self.valores[0], otro.valores[0]))


class Polinomio(Matriz):
    def __init__(self, valores):
        super().__init__(1, len(valores), [list(valores)])

    def dim(self):
        return self.m

    def __str__(self):
        terminos = []
        for exponente, coeficiente in enumerate(self.valores[0]):
            if coeficiente == 0:
                continue
            if exponente == 0:
                termino = str(coeficiente)
            elif exponente == 1:
                termino = f"{coeficiente}x"
            else:
                termino = f"{coeficiente}x^{exponente}"
            terminos.append(termino)
        return "+".join(terminos).replace("+-", "-") if terminos else "0"


if __name__ == "__main__":
    print(Polinomio([1, 2, 3, 4]))
