class House:
    def __init__(self):
        self.__furnished = True

    @property
    def furnished(self):
        return self.__furnished


if __name__ == "__main__":
    house = House()
    print(house.furnished)
