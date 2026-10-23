# Salida esperada:
# Intentemos dividir.
# Se produjo un error.
# Fin del programa.

try:
    print("Intentemos dividir.")
    resultado = 10 / 0
    print("División exitosa.")
except:
    print("Se produjo un error.")
    print("Fin del programa.")
