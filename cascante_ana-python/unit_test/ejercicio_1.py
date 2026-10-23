vitb12_mg = {
    "higado": 75,
    "riñones": 31,
    "sardinas": 28
}


def print_food_b12(food):
    if food in vitb12_mg:
        print("La cantidad de microgramos de vitamina b12 del alimento "
              + food + " es " + str(vitb12_mg[food]))
    else:
        raise KeyError(food + " no es un alimento del catálogo")


if __name__ == "__main__":
    print_food_b12("higado")
    print_food_b12("sardinas")
    try:
        print_food_b12("brocoli")
    except KeyError as e:
        print(e)
