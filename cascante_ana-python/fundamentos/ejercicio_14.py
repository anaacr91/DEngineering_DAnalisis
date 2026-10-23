def invert(cadena):
    """Invierte una cadena de forma recursiva."""
    if len(cadena) <= 1:
        return cadena
    return invert(cadena[1:]) + cadena[0]


if __name__ == "__main__":
    print(invert("hola"))    # aloh
    print(invert("Python"))  # nohtyP
    print(invert("a"))       # a
    print(invert(""))        # cadena vacía
