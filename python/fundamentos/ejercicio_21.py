def count_letter(texto, letra):
    """Cuenta recursivamente una letra sin distinguir mayúsculas y minúsculas."""
    if texto == "" or letra == "":
        return 0
    if len(texto) == 1:
        return 1 if texto.lower() == letra.lower() else 0
    coincidencia = 1 if texto[0].lower() == letra.lower() else 0
    return coincidencia + count_letter(texto[1:], letra)


if __name__ == "__main__":
    print(count_letter("Hola Mundo", "o"))       # 2
    print(count_letter("Recursividad", "r"))     # 2
    print(count_letter("Python es genial", "p")) # 1
    print(count_letter("AAAaaa", "a"))           # 6
    print(count_letter("", "x"))                 # 0
