# lib/book.py

class Book:
    def __init__(self, title, author, isbn, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title must be a non-empty string.")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Author must be a non-empty string.")
        self._author = value

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("ISBN must be a non-empty string.")
        self._isbn = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Price must be a non-negative number.")
        self._price = value