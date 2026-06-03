from Recipe import Recipe


class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients=None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    # def add_ingredient(self, ingredient):
    #     super().add_ingredient(ingredient)
    #
    # @staticmethod
    # def is_valid_ratio(ratio):
    #     super().is_valid_ratio(ratio)

    def scale(self, ratio):
        scaled_recipe = super().scale(ratio)
        return DietaryRecipe(self.title, self.diet_type, scaled_recipe.ingredients)

    def __str__(self):
        old_str = super().__str__()
        return old_str[:10] + " " + self.diet_type + old_str[10:]