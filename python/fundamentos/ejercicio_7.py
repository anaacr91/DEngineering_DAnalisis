# Cubos de los números impares comprendidos entre 1 y 25.
cubos_impares = [n ** 3 for n in range(1, 26) if n % 2 != 0]

if __name__ == "__main__":
    print(cubos_impares)
