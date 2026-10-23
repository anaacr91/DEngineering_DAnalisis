def split(cadena, separador):
    """Divide una cadena usando un separador sin utilizar str.split()."""
    if separador == "":
        raise ValueError("El separador no puede ser una cadena vacía")
    if cadena == "":
        return [""]
    if separador not in cadena:
        return [cadena]

    resultado = []
    inicio = 0
    while True:
        posicion = cadena.find(separador, inicio)
        if posicion == -1:
            resultado.append(cadena[inicio:])
            break
        resultado.append(cadena[inicio:posicion])
        inicio = posicion + len(separador)
    return resultado


if __name__ == "__main__":
    print(split("hola mundo hola", " "))
    print(split("hola,mundo,hola", ","))
    print(split("uno,dos,tres,", ","))
    print(split(",uno,dos,tres", ","))
    print(split("abc", ","))
    print(split("", ","))
    print(split("apple//banana//cherry", "//"))
