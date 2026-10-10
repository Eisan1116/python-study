#1
class Record:
    count = 0
    def __init__(self, date, item, amount):
        Record.count += 1
        self.number = Record.count
        self.date = date
        self.item = item
        self._amount = 0
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

    def show(self):
        print(f"No.{self.number} {self.date} {self.item} {self.amount}円")

#2
class Kakeibo:
    def __init__(self, owner):
        self.owner = owner
        self._records = []

    def add(self, record):
        self._records.append(record)

    @property
    def total(self):
        total = 0
        for record in self._records:
            total += record.amount
        return total

    def show_all(self):
        print(f"=== {self.owner}の家計簿 ===")
        for record in self._records:
            record.show()
        print(f"合計:{self.total}円")

    def __len__(self):
        return len(self._records)

    def __str__(self):
        return f"{self.owner}の家計簿（{len(self)}件・合計{int(self.total / 1000)},{int(self.total % 1000):03d}円）"

k = Kakeibo("瑛心")
k.add(Record("2026-10-10", "昼食", 800))
k.add(Record("2026-10-10", "電車代", 320))
k.add(Record("2026-10-11", "参考書", 2800))
k.add(Record("2026-10-11", "不明", -500))

print(len(k))   # 4
print(k)        # 瑛心の家計簿（4件・合計3,920円）