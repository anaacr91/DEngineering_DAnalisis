import random

# Genera 20 enteros aleatorios entre -10 y 10 y filtra los positivos impares.
numeros = [random.randint(-10, 10) for _ in range(20)]
positivos_impares = list(filter(lambda n: n > 0 and n % 2 != 0, numeros))

if __name__ == "__main__":
    print("Números:", numeros)
    print("Positivos impares:", positivos_impares)
