class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            print("入金額は１円以上にしてください")
            return
        self._balance += amount

    def withdraw(self,amount):
        if amount > self._balance:
            print("残高不足です")
            return
        self._balance -= amount

acc = BankAccount("瑛心")
acc.deposit(10000)
acc.withdraw(3000)
acc.withdraw(50000)     # 残高不足です
acc.deposit(-100)       # 入金額は1円以上にしてください
print(acc.balance)      # 7000
