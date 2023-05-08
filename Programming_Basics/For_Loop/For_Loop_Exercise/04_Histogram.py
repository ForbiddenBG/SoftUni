n = int(input())

group1_counter = 0
group2_counter = 0
group3_counter = 0
group4_counter = 0
group5_counter = 0

for i in range(0, n):
    number = int(input())

    if number < 200:
        group1_counter += 1
    if 200 <= number < 400:
        group2_counter += 1
    if 400 <= number < 600:
        group3_counter += 1
    if 600 <= number < 800:
        group4_counter += 1
    if 800 <= number:
        group5_counter += 1

percent1 = (group1_counter / n) * 100
percent2 = (group2_counter / n) * 100
percent3 = (group3_counter / n) * 100
percent4 = (group4_counter / n) * 100
percent5 = (group5_counter / n) * 100

print(f"{percent1:.2f}%")
print(f"{percent2:.2f}%")
print(f"{percent3:.2f}%")
print(f"{percent4:.2f}%")
print(f"{percent5:.2f}%")
