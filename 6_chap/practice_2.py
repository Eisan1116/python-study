try:
    a = int(input("割られる数を入力してください："))
    b = int(input("割る数を入力してください："))
    c = a / b
except ValueError:
    print("数字を入力してください")
except ZeroDivisionError:
    print("0で割ることはできません")
else:
    print(f"結果：{c}")
finally:
    print("計算処理を終了します")
    
