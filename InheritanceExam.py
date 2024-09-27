# Parent class
class Item:
    #Class level attribute
    pay_discount_rate=0.8
    # Constructor (dunder method)
    def __init__(self, name: str, price: float, quantity=0):
        # Validation
        assert price >= 0, f"Price must be greater than or equal to zero"
        assert quantity >= 0, f"Quantity must be greater than or equal to zero"

        # Instance variables
        self.name = name
        self.price = price
        self.quantity = quantity

    # Method to calculate total price
    def calculate_total_price(self):
        return self.price * self.quantity
    def discount(self):
      #  assert 0 <= pay_discount_rate <= 1, "Discount rate must be between 0 and 1"
        self.price=self.price*self.pay_discount_rate

    # Method to apply a discount
    #def apply_discount(self, discount_rate):

      #  self.price = self.price * (1 - discount_rate)


# Child class (inherits from Item)
class ElectronicItem(Item):
    def __init__(self, name: str, price: float, quantity=0, warranty_period=1):
        # Call the constructor of the parent class using super()
        super().__init__(name, price, quantity)
        # Additional attribute specific to the child class
        self.warranty_period = warranty_period

    # Method to display warranty details
    def display_warranty(self):
        print(f"Item: {self.name} | Warranty Period: {self.warranty_period} years")

    def apply_discount(self):
        super().discount()

# Creating objects from both the parent and child classes
item1 = Item("Book", 15, 3)
print(f"{item1.name} Total Price: ${item1.calculate_total_price()}")

item2 = ElectronicItem("Phone", 1000, 2, warranty_period=2)
print(f"{item2.name} Total Price: ${item2.calculate_total_price()}")
item2.display_warranty()

item3 = ElectronicItem("Laptop", 1500, 1)
print(f"{item3.name} Total Price: ${item3.calculate_total_price()}")
item3.apply_discount()
print(f"Price after discount for {item3.name}: ${item3.price}")
item3.display_warranty()
