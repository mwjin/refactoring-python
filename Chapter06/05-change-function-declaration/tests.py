import math

from address import Address
from book import Book
from circum import circum
from customer import Customer
from in_new_england import xx_in_new_england


def test_circum():
    assert circum(3) == 2 * math.pi * 3


def test_book_add_reservation():
    book = Book()
    book.add_reservation("Minwoo Jeong", False)
    assert "Minwoo Jeong" in book.reservations


def test_in_new_england():
    customer_new_england = Customer(Address("MA"))
    customer_korea = Customer(Address("KO"))
    assert xx_in_new_england(customer_new_england.address.state)
    assert not xx_in_new_england(customer_korea.address.state)
