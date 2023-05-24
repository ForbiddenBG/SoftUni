capacity = float(input())

used_value = 0
counter = 0

data = input()
while data != "End":
    volume = float(data)
    counter += 1
    if counter % 3 == 0:
        volume *= 1.1

    if volume > capacity:
        counter -= 1
        break

    capacity -= volume
    data = input()

if data == "End":
    print(f"Congratulations! All suitcases are loaded!")
else:
    print(f"No more space!")

print(f"Statistic: {counter} suitcases loaded.")