import os 
import shutil
exe_path = os.path.dirname(__file__)
data_file = os.path.join(exe_path, "data.txt")

with open(data_file, "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)

with open(data_file, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

memo_file = os.path.join(exe_path, "memo.txt")
with open(memo_file, "w", encoding="utf-8") as f:
    f.write("1行目\n")
    f.write("2行目\n")

with open(memo_file, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

os.makedirs(os.path.join(exe_path, "backup"), exist_ok=True)
shutil.copy(memo_file, os.path.join(exe_path, "backup", "memo_backup.txt"))