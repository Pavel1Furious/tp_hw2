import pytest

from ShoppingList import ShoppingList
from Recipe import Recipe
from Ingredient import Ingredient

@pytest.fixture
def first_recipe():
    return Recipe("Блюдо 1", [Ingredient("Мука", 500, "г"),
                              Ingredient("Сахар", 100, "кг")])

@pytest.fixture
def second_recipe():
    return Recipe("Блюдо 2", [Ingredient("Мука", 1000, "г"),
                              Ingredient("Апельсин", 10, "мг")])

def test_add(first_recipe, second_recipe):
    shopping_list = ShoppingList()
    shopping_list.add_recipe(first_recipe, 1)
    assert str(shopping_list._items[0]) == "(Ingredient:('Мука', 500.0, 'г'), 'Блюдо 1')"
    assert str(shopping_list._items[1]) == "(Ingredient:('Сахар', 100.0, 'кг'), 'Блюдо 1')"

    with pytest.raises(ValueError):
        shopping_list.add_recipe(second_recipe, -5)

    with pytest.raises(ValueError):
        shopping_list.add_recipe(second_recipe, 0)

def test_remove(first_recipe, second_recipe):
    shopping_list = ShoppingList()
    shopping_list.add_recipe(first_recipe, 1)
    shopping_list.add_recipe(second_recipe, 2)
    shopping_list.remove_recipe("Блюдо 1")
    for i in range(len(shopping_list._items)):
        assert shopping_list._items[i][1] == "Блюдо 2"

    shopping_list.remove_recipe("Несуществующее блюдо")

def test_list(first_recipe, second_recipe):
    shopping_list = ShoppingList()
    shopping_list.add_recipe(first_recipe, 1)
    shopping_list.add_recipe(second_recipe, 2)
    shopping_list_list = shopping_list.get_list()
    assert shopping_list_list[0].name <= shopping_list_list[1].name <= shopping_list_list[2].name
    assert shopping_list_list[1].quantity == 2500

def test_sum(first_recipe, second_recipe):
    first_shopping_list = ShoppingList()
    first_shopping_list.add_recipe(first_recipe, 1)

    second_shopping_list = ShoppingList()
    second_shopping_list.add_recipe(second_recipe, 2)

    sum_shopping_list = first_shopping_list + second_shopping_list
    assert str(first_shopping_list._items[0]) == "(Ingredient:('Мука', 500.0, 'г'), 'Блюдо 1')"
    assert str(second_shopping_list._items[0]) == "(Ingredient:('Мука', 2000.0, 'г'), 'Блюдо 2')"

    sum_shopping_list_list = sum_shopping_list.get_list()
    assert sum_shopping_list_list[1].quantity == 2500