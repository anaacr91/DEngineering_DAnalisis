def my_index(l, a):
    """Devuelve el índice de la primera aparición de a, o -1 si no existe."""
    def buscar(resto, elemento, indice):
        if not resto:
            return -1
        if resto[0] == elemento:
            return indice
        return buscar(resto[1:], elemento, indice + 1)

    return buscar(l, a, 0)


if __name__ == "__main__":
    print(my_index([2, 3, 33, 44, 1], 44))  # 3
    print(my_index([2, 3, 33], 9))          # -1
