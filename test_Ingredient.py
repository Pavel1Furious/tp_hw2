import pytest
from Ingredient import Ingredient


@pytest.fixture
def first_ingredient():
    return Ingredient("Мука", 500, "г")

@pytest.fixture
def second_ingredient():
    return Ingredient("Сахар", 100, "кг")

def test_init(first_ingredient, second_ingredient):
    assert first_ingredient.name == "Мука"
    assert first_ingredient.quantity == 500
    assert first_ingredient.unit == "г"

    assert second_ingredient.name == "Сахар"
    assert second_ingredient.quantity == 100
    assert second_ingredient.unit == "кг"

def test_str(first_ingredient, second_ingredient):
    assert str(first_ingredient) == "Мука: 500.0 г"
    assert str(second_ingredient) == "Сахар: 100.0 кг"

def test_eq(first_ingredient, second_ingredient):
    first_ingredient_copy = Ingredient("Мука", 400, "г")
    assert first_ingredient == first_ingredient_copy

    first_ingredient_renamed = Ingredient("Соль", 500, "г")
    assert first_ingredient != first_ingredient_renamed

    second_ingredient_reunited = Ingredient("Сахар", 100, "мг")
    assert second_ingredient != second_ingredient_reunited