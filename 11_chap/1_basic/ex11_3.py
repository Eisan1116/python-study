class Animal:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"私は{self.name}です")

class Dog(Animal):
    def introduce(self):
        print(f"私は犬の{self.name}です")
    
    def speak(self):
        print(f"{self.name}:ワン！")
    

class Cat(Animal):
    def speak(self):
        print(f"{self.name}:ニャー！")

a = Dog("ポチ")
a.introduce()  # 私はポチです

b = Cat("タマ")
b.introduce()  # 私はタマです
