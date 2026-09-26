'''
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("START")
        result = func(*args, **kwargs)
        print("END")
        return  result
    return wrapper

@simple_decorator
def greet():
    return "こんにちは"

print(greet())

@simple_decorator
def multiply(a, b):
    return a * b

print(multiply(3, 4))

def double_result(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper

@double_result
def add(a, b):
    return a + b

print(add(3, 5))
'''

def log_call(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}が呼ばれました")
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

print(add(3,5))