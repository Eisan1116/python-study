import os
edit_dir = os.path.dirname(__file__)


def save_scores(filename, scores):
    file_path = os.path.join(edit_dir, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        for name, score in scores.items():
            f.write(f"{name}:{score}\n")

def load_scores(filename):
    file_path = os.path.join(edit_dir, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())

scores = {"田中": 80, "鈴木": 92}

save_scores("scores.txt", scores)
load_scores("scores.txt")
