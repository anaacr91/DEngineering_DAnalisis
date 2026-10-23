def delete(l, a):
    """Elimina la primera aparición de a; si no existe, deja la lista igual."""
    if not l:
        return []
    if l[0] == a:
        return l[1:]
    return [l[0]] + delete(l[1:], a)


if __name__ == "__main__":
    print(delete([1, 2, 3, 2], 2))  # [1, 3, 2]
    print(delete([1, 2, 3], 8))     # [1, 2, 3]
