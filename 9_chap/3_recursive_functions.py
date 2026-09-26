#1
def  sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)

print(sum_n(5))

#2
def reverse_str(str):
    if len(str) == 1:
        return str[0]
    return str[-1] + reverse_str(str[0:-1])

print(reverse_str("abc"))

#3
def  find_max(nums):
    if len(nums) == 1:
        return nums[0]
    rest_max = find_max(nums[1:])
    if nums[0] > rest_max:
        return nums[0]
    else:
        return rest_max

print(find_max([3, 20, 2, 9, 4]))

#4
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(2))