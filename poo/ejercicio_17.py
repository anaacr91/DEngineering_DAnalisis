from abc import ABC, abstractmethod

class Matriz(ABC):
    def __init__(self, n, m, valores=None):
        self.n = n
        self.m = m
        self.valores = valores if valores is not None else [[0 for _ in range(m)] for _ in range(n)]

    @abstractmethod
    def dim(self):
        pass
