from abc import ABC, abstractmethod
class Record(ABC):
    kind = "記録"

    def __init__(self, date, amount, memo):
        self.date = date
        self._amount = 0
        self.amount = amount
        self.memo = memo

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError("金額は0以上にしてください")
        self._amount = value
    
    @abstractmethod
    def signed_amount(self):
        pass

    def __str__(self):
        return f"{self.date} {self.kind} {self.amount:,}円 {self.memo}"
    
    def __lt__(self, other):
        return self.date < other.date

class Income(Record):
    kind = "収入"

    def signed_amount(self):
        return self.amount

class Expense(Record):
    kind = "支出"
    def __init__(self, date, amount, memo, category):
        super().__init__(date, amount, memo)
        self.category = category

    def signed_amount(self):
        return -self.amount

    def __str__(self):
        return f"{super().__str__()} [{self.category}]"

class Kakeibo():
    def __init__(self):
        self.records = []
    
    def add(self, record):
        if not isinstance(record, Record):
            raise TypeError("Recordのインスタンスのみ追加できます")
        self.records.append(record)

    def __len__(self):
        return len(self.records)

    def balance(self):
        total = 0
        for record in self.records:
            total += record.signed_amount()
        return total

    def expenses_by_category(self):
        result = {}
        for record in self.records:
            if isinstance(record, Expense):
                result[record.category] = result.get(record.category, 0) + record.amount
        return result

k = Kakeibo()
k.add(Income("2026-10-01", 80000, "バイト代"))
k.add(Expense("2026-10-03", 1200, "昼ごはん", "食費"))
k.add(Expense("2026-10-02", 3500, "参考書", "教育"))
k.add(Expense("2026-10-05", 800, "コンビニ", "食費"))

for r in sorted(k.records):
    print(r)
print(len(k))
print(f"残高: {k.balance():,}円")
print(k.expenses_by_category())

try:
    Record("2026-10-06", 100, "テスト")
except TypeError:
    print("Recordは直接作れない")

try:
    Income("2026-10-06", -500, "テスト")
except ValueError as e:
    print(f"金額エラー: {e}")

try:
    k.add("文字列")
except TypeError as e:
    print(f"追加エラー: {e}")
