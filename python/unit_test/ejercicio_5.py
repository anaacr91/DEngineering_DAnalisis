audi_prices = {
    "e-tron": 130000,
    "q5": 60000,
    "a1": 30000,
}


def display_discounted_price(car, discount):
    full_price = audi_prices[car]
    discount_percentage = discount / 100
    discounted_price = full_price - (full_price * discount_percentage)
    print("The car's discounted price is: " + str(discounted_price))


if __name__ == "__main__":
    car = "q5"
    discount = "20"
    try:
        display_discounted_price(car, discount)
    except KeyError:
        print("Se introdujo un coche no disponible")
    except TypeError:
        print("¡El porcentaje de descuento debe ser un número!")
    except Exception as e:
        print("¡Se encontró una excepción distinta de KeyError y TypeError!", type(e).__name__)
