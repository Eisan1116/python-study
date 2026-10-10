class Member:
    count = 0
    def __init__(self, name):
        self.name = name
        Member.count += 1
        self.number = Member.count

    def show(self):
        print(f"No.{self.number} {self.name}")

m1 = Member("Alice")
m2 = Member("Bob")

m1.show()
m2.show()