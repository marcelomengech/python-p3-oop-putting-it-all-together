# testing/shoe_test.py

import pytest
from lib.shoe import Shoe

def test_shoe_initialization():
    shoe = Shoe("Nike", 10, "Black", 89.99)
    assert shoe.brand == "Nike"
    assert shoe.size == 10
    assert shoe.color == "Black"
    assert shoe.price == 89.99

def test_invalid_brand():
    with pytest.raises(ValueError):
        Shoe("", 10, "Black", 89.99)

def test_invalid_size():
    with pytest.raises(ValueError):
        Shoe("Nike", "Ten", "Black", 89.99)

def invalid_color():
    with pytest.raises(ValueError):
        Shoe("Nike", 10, "", 89.99)

def test_invalid_price():
    with pytest.raises(ValueError):
        Shoe("Nike", 10, "Black", -89.99)