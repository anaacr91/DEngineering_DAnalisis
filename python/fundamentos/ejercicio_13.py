def first_notempty(cadena, indice=0):
    """Devuelve el índice del primer carácter que no sea espacio; -1 si no hay."""
    if indice >= len(cadena):
        return -1
    if cadena[indice] != " ":
        return indice
    return first_notempty(cadena, indice + 1)


if __name__ == "__main__":
    print(first_notempty("   hola mundo"))  # 3
    print(first_notempty("hola"))          # 0
    print(first_notempty(" "))             # -1
    print(first_notempty(""))              # -1
