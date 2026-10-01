#1
def total(*nums):
    return sum(nums)
print(total(1, 2, 3, 4))

#2
words = ["apple", "kiwi", "banana", "fig", "grape"]
five_letter_words = [word for word in words if len(word) >= 5]
print(five_letter_words)

items = [
    {"name": "A", "stock": 3},
    {"name": "B", "stock": 10},
    {"name": "C", "stock": 1},
]

#3
sorted_items = sorted(items, key=lambda x:x["stock"], reverse = True)
print(sorted_items)

#4
def product(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] * product(nums[1:])

print(product([2, 3, 4]))

#5
count = 0
def count_calls(func):
    def wrapper(*args, **kwargs):
        global count
        count += 1
        print(f"{count}回目です")
        return func(*args, **kwargs)
    return wrapper

@count_calls
def say_hi():
    print("Hi")

say_hi()
say_hi()
say_hi()