class Record:
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if not isinstance(value, int) or value < 0:
            print("金額は0以上の整数で入力してください")
            return
        self._amount = value

r = Record("昼食", 800)
print(r.amount)      # 800
r.amount = -100      # 金額は0以上の整数で入力してください
r.amount = "千円"    # 金額は0以上の整数で入力してください
print(r.amount)      # 800