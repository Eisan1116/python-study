def create_profile(name, age=18, *hobbies, **extra_info):
    print(f"名前：{name}")
    print(f"年齢：{age}")
    for num, hobby in enumerate(hobbies):
        print(f"趣味{num+1}：{hobby}")
    for key, value in extra_info.items():
        print(f"{key}：{value}")

create_profile("瑛心", 19, "読書", "プログラミング", 出身="千葉", 大学="○○大学")