from restaurant.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    __COFFEE_MILLILITERS = 50
    __COFFEE_PRICE = 3.50

    def __init__(self, name, caffeine):
        super().__init__(name, 0, 0)
        self.caffeine = caffeine

    def milliliters(self):
        return self.__COFFEE_MILLILITERS

    def price(self):
        return self.__COFFEE_PRICE

    def caffeine(self):
        return self.caffeine


# coffee = Coffee("black", 20)
# print(coffee.name)
# print(coffee.milliliters)
# print(coffee.price)
# print(coffee.caffeine)
