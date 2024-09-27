from msilib.schema import Property


class Item:
    #constrcutor creation
    def __init__(self,name:str,price:float,quantity=0):#magical method ,dunder method
    #Validation
        assert price>=0 , f"price is always greater than or equal to zero"
        assert quantity >=0
        self.name=name
        self.price=price
        self.quantity=quantity
    #defining calculate_total_price function
    def calculate_total_price(self):
        return self.price*self.quantity
        # object for this class
#Creating the object
item1 = Item("phone",-1000,2)
print(item1.calculate_total_price())
item2=Item("laptop",300,3)
print(item2.calculate_total_price())
item3=Item("Mouse",20,4)
print(item3.calculate_total_price())