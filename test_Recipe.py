import pytest

from Ingredient import Ingredient
from Recipe import Recipe

@pytest.fixture
def first_ingredient():
    return Ingredient("Мука", 500, "г")

@pytest.fixture
def second_ingredient():
    return Ingredient("Сахар", 100, "кг")

@pytest.fixture
def third_ingredient():
    return Ingredient("Мука", 1000, "г")

@pytest.fixture
def fourth_ingredient():
    return Ingredient("Соль", 10, "мг")

def test_init(first_ingredient, second_ingredient):
    recipe = Recipe("Блюдо", [first_ingredient, second_ingredient])
    assert recipe.title == "Блюдо"
    assert recipe.ingredients[0] == first_ingredient and recipe.ingredients[1] == second_ingredient

def test_add(first_ingredient, second_ingredient, third_ingredient, fourth_ingredient):
    recipe = Recipe("Блюдо", [first_ingredient, second_ingredient])
    recipe.add_ingredient(fourth_ingredient)
    assert recipe.ingredients[2] == fourth_ingredient

    recipe.add_ingredient(third_ingredient)
    assert recipe.ingredients[0].quantity == 1500

def test_scale(first_ingredient, second_ingredient):
    recipe = Recipe("Блюдо", [first_ingredient, second_ingredient])
    scaled_recipe = recipe.scale(10)
    assert recipe.ingredients[0].quantity != 5000 and scaled_recipe.ingredients[0].quantity == 5000
    assert recipe.ingredients[1].quantity != 1000 and scaled_recipe.ingredients[1].quantity == 1000
    assert recipe != scaled_recipe

    with pytest.raises(ValueError):
        recipe.scale(-10)

    with pytest.raises(ValueError):
        recipe.scale(0)

def test_len(first_ingredient, second_ingredient, third_ingredient, fourth_ingredient):
    recipe = Recipe("Блюдо")
    assert len(recipe) == 0

    recipe.add_ingredient(first_ingredient)
    assert len(recipe) == 1

    recipe.add_ingredient(second_ingredient)
    assert len(recipe) == 2

    recipe.add_ingredient(third_ingredient)
    assert len(recipe) == 2

    recipe.add_ingredient(fourth_ingredient)
    assert len(recipe) == 3