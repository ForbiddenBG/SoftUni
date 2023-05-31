num = int(input())
multiplier = int(input())

total = 0

while True:
    total = num * multiplier
    if multiplier > 10:
        print(f"{num} X {multiplier} = {total}")
        break
    if multiplier == 10:
        print(f"{num} X {multiplier} = {total}")
        break
    print(f"{num} X {multiplier} = {total}")
    multiplier += 1
