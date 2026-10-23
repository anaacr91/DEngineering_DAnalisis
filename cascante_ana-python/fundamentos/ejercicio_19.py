def upper(cadena):
    """Convierte letras ASCII minúsculas a mayúsculas usando chr() y ord()."""
    resultado = ""
    for caracter in cadena:
        codigo = ord(caracter)
        if ord("a") <= codigo <= ord("z"):
            resultado += chr(codigo - (ord("a") - ord("A")))
        else:
            resultado += caracter
    return resultado


if __name__ == "__main__":
    print(upper("hola mundo"))  # HOLA MUNDO
    print(upper("Python3.9"))   # PYTHON3.9
    print(upper("123abc!"))     # 123ABC!
    print(upper(""))            # cadena vacía
    print(upper("MAYUS"))       # MAYUS
