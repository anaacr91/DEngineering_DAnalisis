def f1(cadena):
    return cadena[::-1]


def f2(cadena):
    for i, char in enumerate(cadena):
        if char != " ":
            return i
    return len(cadena)


def strip(cadena):
    """Elimina espacios al principio y al final sin usar str.strip()."""
    inicio = f2(cadena)
    if inicio == len(cadena):
        return ""
    invertida = f1(cadena)
    final_invertido = f2(invertida)
    fin = len(cadena) - final_invertido
    return cadena[inicio:fin]


if __name__ == "__main__":
    print(strip(" hola mundo "))  # hola mundo
    print(strip("hola"))         # hola
    print(strip(" "))             # cadena vacía
    print(strip(""))              # cadena vacía
