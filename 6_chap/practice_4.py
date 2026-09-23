menu = {"コーヒー":400, "紅茶" :350, "抹茶": 450}
print(menu.get("ジュース", "取り扱いなし"))

for key, value in menu.items():
    print(f"{key}:{value}円")

menu["ラテ"] = 500
menu["紅茶"] = 380
del menu["抹茶"]
print(menu.items())
