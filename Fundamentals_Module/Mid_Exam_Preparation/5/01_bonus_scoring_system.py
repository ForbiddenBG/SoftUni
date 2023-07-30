students_count = int(input())
lectures_count = int(input())
add_bonus = int(input())

max_num = 0
atten = 0

for student in range(students_count):
    attendance = int(input())
    total_bonus = (attendance / lectures_count) * (5 + add_bonus)
    if max_num < total_bonus:
        max_num = total_bonus
        atten = attendance

print(f"Max Bonus: {round(max_num)}.")
print(f"The student has attended {atten} lectures.")
