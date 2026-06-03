from Ingredient import Ingredient


class Recipe:
    def __init__(self, title, ingredients=None):
        if ingredients is None:
            ingredients = []
        self.title = title
        self.ingredients = ingredients

    def add_ingredient(self, ingredient):
        for i in range(len(self.ingredients)):
            current_ingredient = self.ingredients[i]
            if current_ingredient == ingredient:
                updated_ingredient = Ingredient(ingredient.name, ingredient.quantity
                                                + current_ingredient.quantity, ingredient.unit)
                self.ingredients[i] = updated_ingredient
                break
        else:
            self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if type(ratio) in [float, int]:
            if float(ratio) > 0:
                return True
        return False

    def scale(self, ratio):
        new_ingredients_list = []
        for i in range(len(self.ingredients)):
            current_ingredient = self.ingredients[i]
            new_ingredient = Ingredient(current_ingredient.name,
                                        current_ingredient.quantity * ratio, current_ingredient.unit)
            new_ingredients_list.append(new_ingredient)
        new_recipe = Recipe(self.title, new_ingredients_list)
        return new_recipe

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        str_ingredients = ""
        for i in range(len(self.ingredients)):
            str_ingredients += (f"Ingredient {i + 1}: {self.ingredients[i].name}, "
                                f"{self.ingredients[i].quantity}, {self.ingredients[i].unit}, ")
        return "Dish name: " + self.title + "; " + str_ingredients