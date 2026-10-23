def belong(l, a):
    """Devuelve True si a pertenece a l, usando recursividad y ==."""
    if not l:
        return False
    if l[0] == a:
        return True
    return belong(l[1:], a)


if __name__ == "__main__":
    print(belong([1, 2, 3], 2))  # True
    print(belong([1, 2, 3], 5))  # False
