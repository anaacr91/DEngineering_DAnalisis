def col_recursiva(m, i):
    """Versión recursiva de col; lanza IndexError si el índice no existe."""
    if not m:
        return []
    if i < 0 or i >= len(m[0]):
        raise IndexError("El índice excede las dimensiones de la matriz")
    return [m[0][i]] + col_recursiva(m[1:], i)


if __name__ == "__main__":
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(col_recursiva(matriz, 1))  # [2, 5, 8]
    # print(col_recursiva(matriz, 3))  # Lanza IndexError
