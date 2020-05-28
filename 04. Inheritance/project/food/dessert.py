from restaurant.food.food import Food


class Dessert(Food):
    def __init__(self, name, price, grams, calories):
        super().__init__(name, price, grams)
        self.calories = calories


    def get_calories(self):
        return self.calories

