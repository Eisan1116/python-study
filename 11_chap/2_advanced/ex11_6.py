class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return int(self.price * 1.1)

class FoodProduct(Product):
    def price_with_tax(self):
        return int(self.price * 1.08)

p = Product("ノート", 200)
f = FoodProduct("おにぎり", 150)
print(p.price_with_tax())   # 220
print(f.price_with_tax())   # 162