def es_palindromo(texto):
    """Devuelve True si el texto es palíndromo, ignorando espacios y mayúsculas."""
    normalizado = "".join(caracter.lower() for caracter in texto if not caracter.isspace())
    return normalizado == normalizado[::-1]


if __name__ == "__main__":
    print(es_palindromo("Anita lava la tina"))  # True
    print(es_palindromo("Python"))              # False
