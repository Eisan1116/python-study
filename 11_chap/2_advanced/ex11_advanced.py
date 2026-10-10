class Record:
    def __init__(self, date, item, amount):
        self.date = date
        self.item = item
        self.amount = amount

    def show(self):
        print(f"{self.date} {self.item} {self.amount}円")


class Expense(Record):
    def __init__(self, date, item, amount, category):
        super().__init__(date, item, amount)
        self.category = category

    def show(self):
        print(f"{self.date} {self.item} {self.amount}円")   # ← 親と同じ行をもう一度書いている
        print(f"  カテゴリ：{self.category}")

class Record:
    def __init__(self, date, item, amount):
        self.date = date
        self.item = item
        self.amount = amount

    def to_text(self):
        return f"{self.date} {self.item} {self.amount}円"


class Expense(Record):
    def __init__(self, date, item, amount, category):
        super().__init__(date, item, amount)
        self.category = category

    def to_text(self):
        text = super().to_text()               # 親の結果を受け取る
        return f"{text}（{self.category}）"    # 加工して返す


e = Expense("2026-10-10", "昼食", 800, "食費")
print(e.to_text())   # 2026-10-10 昼食 800円（食費）

class Record:                      # 親
    ...

class Expense(Record):             # 子
    ...

class FixedExpense(Expense):       # 孫（毎月の固定費）
    def __init__(self, date, item, amount, category, day):
        super().__init__(date, item, amount, category)   # 親（Expense）に任せる
        self.day = day                                    # 毎月の支払日