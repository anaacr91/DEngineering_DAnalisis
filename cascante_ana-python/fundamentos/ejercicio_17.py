def replace(cadena, subcadena1, subcadena2):
    """Reemplaza la primera aparición; si subcadena1 es vacía, intercala el texto."""
    if cadena == "" or (subcadena1 != "" and subcadena1 not in cadena):
        return cadena
    if subcadena1 == "":
        resultado = subcadena2
        for caracter in cadena:
            resultado += caracter + subcadena2
        return resultado
    posicion = cadena.find(subcadena1)
    return (cadena[:posicion] + subcadena2 +
            cadena[posicion + len(subcadena1):])


if __name__ == "__main__":
    print(replace("holaquetalestasjoaquin", "joaquin", "jacobo"))
    print(replace("hola mundo, hola a todos", "hola", "hi"))
    print(replace("javascript", "java", "python"))
    print(replace("aaaaa", "a", "b"))
    print(replace("abc d", "", "X"))
    print(replace("abc", "", "X"))
    print(replace("", "a", "b"))
    print(replace("the cat sat on the mat", "cat", "dog"))
    print(replace("abcde fgh", " ", "X"))
