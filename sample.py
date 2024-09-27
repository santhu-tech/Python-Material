class Animal:
    #Constrcutor
    def __init__(self,name):
        self.name=name;
    #function
    def speak(self):
        print(f"{self.name} makes a sound")
#inheritance
class Cat(Animal):
    def speak(self):
        super().speak()
        #print(f"{self.name} meows")
class Dog(Animal):
    def __init__(self,name,breed): #child class constrcutor
        super().__init__(name) #Call the parent constrcutor
        self.breed=breed
    #parent class character
    def speak(self):
        #using super keyword going to call parent method
        super().speak()
        #print(f"{self.name},the{self.breed},barks")
   #child class character
    def eat(self):
        print(f"{self.name} eat only non veg")
#object creation
cat=Cat("snow")
dog=Dog("puppy","Golden reteriver")

#call method
dog.speak()
cat.speak()
dog.eat()
