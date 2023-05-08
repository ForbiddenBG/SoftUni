n = int(input())

group1_counter = 0
group2_counter = 0
group3_counter = 0

for i in range(0, n):
    number = int(input())

    if number % 2 == 0:
        group1_counter += 1

    if number % 3 == 0:
        group2_counter += 1

    if number % 4 == 0:
        group3_counter += 1

percent1 = (group1_counter / n) * 100
percent2 = (group2_counter / n) * 100
percent3 = (group3_counter / n) * 100

print(f"{percent1:.2f}%")
print(f"{percent2:.2f}%")
print(f"{percent3:.2f}%")