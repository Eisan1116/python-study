nums = [1, 2, 3, 4, 5]
twice_nums = list(map(lambda x: x*2 , nums))

nums = [3, 8, 15, 22, 7, 40]
more10_nums = list(filter(lambda x: x > 10, nums))
print(more10_nums)

items = [
    {"name": "ノート", "price": 150},
    {"name": "消しゴム", "price": 50},
    {"name": "ペン", "price": 100},
]

sorted_list = sorted(items, key=lambda x: x["price"])

nums = [1, 2, 3, 4, 5, 6, 7, 8]
new_nums = list(map(lambda x:x ** 2, filter(lambda x : x % 2 == 0, nums)))

students = [("田中", 80), ("佐藤", 80), ("鈴木", 90)]
sorted_students = sorted(students, key = lambda x : (-x[1], x[0]))
