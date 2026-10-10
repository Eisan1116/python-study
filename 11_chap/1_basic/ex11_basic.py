class Expense:                     # 支出
    def __init__(self, date, item, amount):
        self.date = date
        self.item = item
        self.amount = amount

    def show(self):
        print(f"{self.date} {self.item} {self.amount}円")


class Income:                      # 収入
    def __init__(self, date, item, amount):
        self.date = date
        self.item = item
        self.amount = amount

    def show(self):
        print(f"{self.date} {self.item} {self.amount}円")