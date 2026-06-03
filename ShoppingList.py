from hashlib import new

from Ingredient import Ingredient


class ShoppingList:
    def __init__(self, items=None):
        if items is None:
            items = []
        self._items = items

    def add_recipe(self, recipe, portions):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled_recipe = recipe.scale(portions)
        title = scaled_recipe.title
        for ingredient in scaled_recipe.ingredients:
            self._items.append((ingredient, title))

    def remove_recipe(self, title):
        new_items = []
        for i in range(len(self._items)):
            if self._items[i][1] != title:
                new_items.append(self._items[i])
        self._items = new_items

    def get_list(self):
        temp_dict = {}
        for ingredient in self._items:
            temp_key = (ingredient[0].name, ingredient[0].unit)
            if temp_key in temp_dict.keys():
                temp_dict[temp_key] += ingredient[0].quantity
            else:
                temp_dict[temp_key] = ingredient[0].quantity
        res_list = []
        for key, value in temp_dict.items():
            ingredient = Ingredient(key[0], value, key[1])
            res_list.append(ingredient)
        res_list.sort(key=lambda x: x.name)
        return res_list

    def __add__(self, other):
        if type(other) != type(self):
            raise ValueError("Складывать список покупок можно только с другим списком покупок")
        new_items = self._items + other._items
        return ShoppingList(new_items)