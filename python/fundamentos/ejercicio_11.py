def sum_rows(l1, l2):
    """Suma dos listas de la misma longitud usando recursividad."""
    if len(l1) != len(l2):
        raise ValueError("Las listas deben tener la misma longitud")
    if not l1:
        return []
    return [l1[0] + l2[0]] + sum_rows(l1[1:], l2[1:])


if __name__ == "__main__":
    print(sum_rows([9, 99, 999], [1, 1, 1]))  # [10, 100, 1000]
