class Item:
    # Constructor
    def __init__(self, name: str, price: float, quantity=0):
        # Validation for price and quantity
        assert price >= 0, "Price must be greater than or equal to zero"
        assert quantity >= 0, "Quantity must be greater than or equal to zero"

        self.name = name
        self.__price = price  # Private attribute for price
        self.quantity = quantity

    # Getter method for price (read access)
    @property
    def price(self):
        return self.__price

    # Setter method for price (write access)
    @price.setter
    def price(self, value):
        assert value >= 0, "Price must be greater than or equal to zero"
        self.__price = value

    # Method to calculate the total price (uses the encapsulated price)
    def calculate_total_price(self):
        return self.__price * self.quantity


# Create object instances of the Item class
item1 = Item("Tablet", 500, 3)  # Initial price 500, quantity 3
print(f"Initial price of {item1.name}: ${item1.price}")
print(f"Total price before modification: ${item1.calculate_total_price()}")

# Modify the price using the setter
item1.price = 600  # Change price to 600
print(f"Modified price of {item1.name}: ${item1.price}")
print(f"Total price after modification: ${item1.calculate_total_price()}")

class ElectronicItem(Item) :

    def __init__(self, name: str, price: float, quantity=0, warranty_period=1):
        # Call the constructor of the parent class using super()
        super().__init__(name, price, quantity)
        # Additional attribute specific to the child class
        self.warranty_period = warranty_period

tem7 = Item("LAptop",300,4)
print(f"{item1.price}")

tem2=ElectronicItem("Compute",4000,12)
print(f"{tem2.price}")