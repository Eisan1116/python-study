class Animal:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"私は{self.name}です")

class Dog(Animal):
    pass

class Cat(Animal):
    pass