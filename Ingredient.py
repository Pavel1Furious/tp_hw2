class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self.quantity

    @quantity.setter
    def quantity(self, value):
        try:
            float(value)
        except Exception as e:
            raise ValueError("Введенное значение это не число")
        value = float(value)
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        else:
            self._quantity = value

    def __str__(self):
        return self.name + ": " + str(self._quantity) + " " + self.unit

    def __repr__(self):
        return f"Ingredient:('{self.name}', {self._quantity}, '{self.unit}')"

    def __eq__(self, other):
        if type(self) != type(other):
            return ValueError("Можно сравнить ингредиент только с ингредиентом")
        return self.name == other.name and self.unit == other.unit