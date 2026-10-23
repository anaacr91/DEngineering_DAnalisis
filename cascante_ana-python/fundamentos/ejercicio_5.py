def mx(l):
    """Devuelve el mayor elemento de una lista no vacía, sin usar max()."""
    if not l:
        raise ValueError("La lista no puede estar vacía")
    if len(l) == 1:
        return l[0]
    mayor_resto = mx(l[1:])
    return l[0] if l[0] > mayor_resto else mayor_resto


if __name__ == "__main__":
    print(mx([4, 9, 2, 7]))  # 9
