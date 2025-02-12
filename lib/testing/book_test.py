# testing/book_test.py

import pytest
from lib.book import Book

def test_book_initialization():
    book = Book("1984", "George Orwell", "1234567890", 15.99)
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.isbn == "1234567890"
    assert book.price == 15.99

def test_invalid_title():
    with pytest.raises(ValueError):
        Book("", "George Orwell", "1234567890", 15.99)

def test_invalid_author():
    with pytest.raises(ValueError):
        Book("1984", "", "1234567890", 15.99)

def test_invalid_isbn():
    with pytest.raises(ValueError):
        Book("1984", "George Orwell", "", 15.99)

def test_invalid_price():
    with pytest.raises(ValueError):
        Book("1984", "George Orwell", "1234567890", -15.99)