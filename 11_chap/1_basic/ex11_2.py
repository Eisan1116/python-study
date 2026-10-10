class Animal:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"私は{self.name}です")

class Dog(Animal):
    def speak(self):
        print(f"{self.name}:ワン！")
    

class Cat(Animal):
    def speak(self):
        print(f"{self.name}:ニャー！")