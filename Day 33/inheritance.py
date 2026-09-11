# Creating the animal hierarchy using object oriented programing inheritance method.
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        
    def make_sound(self):
        print(f"{self.name} says {self.sound}")
        
class Dog(Animal):
    def run(self):
        print(f"{self.name} is running around the park.")
class Cat(Animal):
    def play(self):
        print(f"{self.name} is playing with the ball.")
class Cow(Animal):
    def graze(self):
        print(f"{self.name} is grazing grass in the field.")
        
dog = Dog("Tuffy", "Woof")
cat = Cat("Kitty", "Meow")
cow = Cow("Vasudha", "Moo")
print(cow.name)
print(cow.sound)
cow.graze()                        