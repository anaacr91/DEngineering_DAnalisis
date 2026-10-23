def sum_matrix(m1, m2):
    """Suma dos matrices de igual dimensión usando recursividad."""
    if len(m1) != len(m2):
        raise ValueError("Las matrices deben tener el mismo número de filas")
    if not m1:
        return []
    if any(len(fila) != len(m1[0]) for fila in m1 + m2):
        raise ValueError("Todas las filas deben tener la misma longitud")
    if any(len(a) != len(b) for a, b in zip(m1, m2)):
        raise ValueError("Las matrices deben tener las mismas dimensiones")
    return [sum_rows(m1[0], m2[0])] + sum_matrix(m1[1:], m2[1:])


def sum_rows(l1, l2):
    if len(l1) != len(l2):
        raise ValueError("Las filas deben tener la misma longitud")
    if not l1:
        return []
    return [l1[0] + l2[0]] + sum_rows(l1[1:], l2[1:])


if __name__ == "__main__":
    print(sum_matrix([[1, 2], [3, 4]], [[10, 20], [30, 40]]))
    # [[11, 22], [33, 44]]
