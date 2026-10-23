def col(m, i):
    """Devuelve la columna i de una matriz representada como lista de listas."""
    if not m:
        return []
    return [fila[i] for fila in m]


if __name__ == "__main__":
    print(col([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))  # [2, 5, 8]
