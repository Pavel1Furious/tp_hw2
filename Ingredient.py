class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if type(value) in [float, int]:
            value = float(value)
            if value <= 0:
                raise ValueError("Количество должно быть положительным")
            else:
                self._quantity = value
        else:
            raise ValueError("Введённое значение это не число")

    def __str__(self):
        return self.name + ": " + str(self._quantity) + " " + self.unit

    def __repr__(self):
        return f"Ingredient:('{self.name}', {self._quantity}, '{self.unit}')"

    def __eq__(self, other):
        if type(self) != type(other):
            return ValueError("Можно сравнить ингредиент только с ингредиентом")
        return self.name == other.name and self.unit == other.unit