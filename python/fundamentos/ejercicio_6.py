def my_order(l):
    """Ordena la lista de menor a mayor recursivamente, usando max() y remove()."""
    if not l:
        return []
    copia = l.copy()
    mayor = max(copia)
    copia.remove(mayor)
    return my_order(copia) + [mayor]


if __name__ == "__main__":
    print(my_order([4, 1, 3, 2]))  # [1, 2, 3, 4]
