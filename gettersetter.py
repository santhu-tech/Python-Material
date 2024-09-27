from collections.abc import async_generator
from msvcrt import locking
from os import waitpid


class Item:
    def __init__(self, name: str, price: float):
        self.name = name  # Public variable
        self.__price = price  # Private variable
    def get_price(self):
        return self.__price
    def set_price(self, value):
        if value < 0:
            print("Price can't be negative. Setting it to 0.")
            self.__price = 0  # Enforce the price to be non-negative
        else:
            self.__price = value
    # Method to display item details
    def display_item_details(self):
        print(f"Item: {self.name}, Price: {self.__price}")
# Creating an object of the Item class
item = Item("Laptop", 1000)
# Accessing the public variable directly
print(item.name)
# Accessing the private variable through the getter method
print(item.get_price())
# Modifying the private variable through the setter method
item.set_price(1200)
print(item.get_price())
# Attempting to set a negative price, which should trigger validation
item.set_price(-500)
print(item.get_price())
# Displaying item details
item.display_item_details()
class BookItem(Item):
    def __init__(self,name,price,ISBN):
        super().__init__(name,price)
    def book_details(self):
        print("book all details ")
        print(f"{self.price}")
book=BookItem("Python programming",1000,233245885)
print(book.name)
print(book.price)
print(book.ISBN)

@staticmethod
@classmethod
@property
@trycatch
@unittest

@async_generator
@locking
@wait