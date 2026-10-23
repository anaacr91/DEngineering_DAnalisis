from abc import ABC, abstractmethod

class Matriz(ABC):
    def __init__(self, n, m, valores=None):
        self.n, self.m = n, m
        self.valores = valores if valores is not None else [[0 for _ in range(m)] for _ in range(n)]
    @abstractmethod
    def dim(self):
        pass

class Vector(Matriz):
    def __init__(self, valores):
        super().__init__(1, len(valores), [list(valores)])
    def dim(self):
        return self.m
