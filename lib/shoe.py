# lib/shoe.py

class Shoe:
    def __init__(self, brand, size, color, price):
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Brand must be a non-empty string.")
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Size must be a number.")
        self._size = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Color must be a non-empty string.")
        self._color = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Price must be a non-negative number.")
        self._price = value