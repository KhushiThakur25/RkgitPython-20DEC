class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I m a cat.My name {self.name} and i m {self.age} years old")
    def sound(self):
        print("Meow")

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I m a dog.My name {self.name} and i m {self.age} years old")
    def sound(self):
        print("bark!")

cat1 = Cat("kitty",2.5)
dog1 = Dog("Jammy",5)

cat2 = Cat("sam",2)
dog2 = Dog("Tom",4)

# cat.info()
# dog.info()

for animal in (cat1,cat2,dog1,dog2):
    animal.info()
    animal.sound()

