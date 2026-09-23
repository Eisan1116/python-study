#1
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))

doubled = [x * 2 for x in nums]

#2
nums = [3, 8, 15, 22, 7, 40]
big_nums = list(filter(lambda x: x > 10, nums))

big_nums = [x for x in nums if x > 10]

#3
nums = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums)))

result = [x ** 2 for x in nums if x % 2 == 0]

#4 
nums = [1, 2, 3, 4, 5]
squared_nums = {x: x ** 2 for x in nums}
