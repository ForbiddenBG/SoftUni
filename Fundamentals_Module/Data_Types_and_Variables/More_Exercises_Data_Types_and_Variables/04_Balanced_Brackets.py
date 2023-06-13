n_lines = int(input())

count_open = 0
count_close = 0
is_balanced = True

for i in range(1, n_lines + 1):
    line = input()

    if line == "(":
        count_open += 1
        if (count_open - count_close) >= 2:
            is_balanced = False
            break
    elif line == ")":
        count_close += 1
    if count_close > count_open:
        is_balanced = False
        break

if count_open != count_close:
    is_balanced = False
if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
