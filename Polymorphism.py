class Item:
    # Constructor
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price should be greater than or equal to zero."
        assert quantity >= 0, f"Quantity should be greater than or equal to zero."
        self.name = name
        self.price = price
        self.quantity = quantity

    # Common method to calculate the total price
    def calculate_total_price(self):
        return self.price * self.quantity


class ElectronicItem(Item):
    # Overriding the calculate_total_price method
    def calculate_total_price(self):
        # Assuming electronics have an extra tax of 10%
        return (self.price * self.quantity) * 1.10


class GroceryItem(Item):
    # No override, it uses the parent class method
    pass


class ClothingItem(Item):
    # Overriding the calculate_total_price method
    def calculate_total_price(self):
        # Assuming clothing has a 5% discount
        return (self.price * self.quantity) * 0.95


# Polymorphism in action
items = [ElectronicItem("Laptop", 1000, 2), GroceryItem("Milk", 3, 10), ClothingItem("T-shirt", 20, 5)]

for item in items:
    print(f"{item.name} Total Price: ${item.calculate_total_price():.2f}")
