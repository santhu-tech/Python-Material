class Dog:
    def sound(self):
        print("Bark")

    def move(self):
        print("Run")


class Cat:
    def sound(self):
        print("Meow")

    def move(self):
        print("Jump")


def animal_actions(animal):
    animal.sound()
    animal.move()
 # animal.sleep()


dog = Dog()
cat = Cat()

animal_actions(dog)
animal_actions(cat)