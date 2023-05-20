import sys

best_player = ""
max_goals = - sys.maxsize
min_goals = sys.maxsize
trick = False

name = input()
while name != "END":
    current_goals = int(input())
    if current_goals > max_goals:
        max_goals = current_goals
        best_player = name
        if 10 > max_goals >= 3:
            trick = True
        elif max_goals >= 10:
            trick = True
            break
    name = input()

if "END":
    print(f"{best_player} is the best player!")
    if trick:
        print(f"He has scored {max_goals} goals and made a hat-trick !!!")
    else:
        print(f"He has scored {max_goals} goals.")
