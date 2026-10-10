class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"『{self.title}』 {int(self.price / 1000)},{int(self.price % 1000):03d}円"

b = Book("独習Python", 3000)
print(b)   # 『独習Python』 3,000円
