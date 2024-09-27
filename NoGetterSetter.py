class Item:
    def __init__(self, name: str, price: float):
        self.name = name  # Public variable
        self.__price = price  # Private variable

    # Method to display item details
    def display_item_details(self):
        print(f"Item: {self.name}, Price: {self.__price}")

# Create an object of Item class
item = Item("Laptop", 1000)

# Public variable access (direct access)
print(item.name)  # Output: Laptop

# Trying to access the private variable directly will raise an error
print(item.__price)  # Raises AttributeError

# Calling the method that uses the private variable internally
item.display_item_details()  # Output: Item: Laptop, Price: 1200
