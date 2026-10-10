class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def show(self):
        print(f"{self.title}:{self.price}円")

b1 = Book("Python Programming", 29.99)
b2 = Book("Data Science with Python", 39.99)
