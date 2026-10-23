def right_append(l, a):
    """Devuelve una nueva lista con a añadido por la derecha, recursivamente."""
    if not l:
        return [a]
    return [l[0]] + right_append(l[1:], a)


if __name__ == "__main__":
    print(right_append([1, 2, 3], 4))  # [1, 2, 3, 4]
