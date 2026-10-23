def endswith(cadena, subcadena):
    """Comprueba si cadena termina en subcadena sin usar str.endswith()."""
    if len(subcadena) > len(cadena):
        return False
    if subcadena == "":
        return True
    return cadena[len(cadena) - len(subcadena):] == subcadena


if __name__ == "__main__":
    print(endswith("hola mundo", "mundo"))  # True
    print(endswith("hola mundo", "hola"))   # False
    print(endswith("python", "on"))         # True
    print(endswith("python", "py"))         # False
    print(endswith("abc", "abcdefg"))       # False
