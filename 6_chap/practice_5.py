list = [x for x in range(1,11)]
print(list)

dic = {x : x ** 2 for x in range(1,6)}

default_settings = {"volume": 50, "brightness": 70, "language": "ja"}
user_settings = {"volume": 80, "theme": "dark"}
final_settings = {**default_settings, **user_settings}
print(final_settings)