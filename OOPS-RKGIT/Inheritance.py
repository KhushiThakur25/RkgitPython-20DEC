class Animal:
    def __init__(self,species):
        self.species = species

    def sound(self):
        return "Some animal's sound"
class Dog(Animal):
    def __init__(self,breed):
        Animal.__init__(self,"Dog")
        self.breed = breed

    def sound(self):
        return "Bark!"

class Cat(Animal):
    def __init__(self,breed):
        Animal.__init__(self,"Cat")
        self.breed = breed

    def sound(self):
        return "Meow!"

dog = Dog("German Shepherd")
cat = Cat("Persian")

print(dog.species)
print(dog.breed)
print(dog.sound())

print(cat.species)
print(cat.breed)
print(cat.sound())

print(super(Cat,cat).sound())

