def son_anagramas(palabra1, palabra2):
    """Comprueba anagramas ignorando espacios y mayúsculas."""
    normalizada1 = sorted(caracter.lower() for caracter in palabra1 if not caracter.isspace())
    normalizada2 = sorted(caracter.lower() for caracter in palabra2 if not caracter.isspace())
    return normalizada1 == normalizada2


if __name__ == "__main__":
    print(son_anagramas("amor", "roma"))           # True
    print(son_anagramas("listen", "silent"))       # True
    print(son_anagramas("python", "typhon"))       # True
    print(son_anagramas("hola", "halo"))           # True
    print(son_anagramas("Anagrama", "Nag a aram")) # True
    print(son_anagramas("pedal", "laaped"))        # False
