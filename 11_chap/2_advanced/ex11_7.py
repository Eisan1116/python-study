class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return int(self.price * 1.1)

class FoodProduct(Product):
    def price_with_tax(self):
        return int(self.price * 1.08)

items = [
    Product("ノート", 200),
    FoodProduct("おにぎり", 150),
    FoodProduct("お茶", 130),
    Product("ペン", 100),
]

total = 0
food_total = 0

for item in items:
    if isinstance(item, FoodProduct):
        total += item.price_with_tax()
        food_total += item.price_with_tax()
    else:
        total += item.price_with_tax()

print(f"食品の税込合計:{food_total}円")
print(f"全商品の税込合計:{total}円")
