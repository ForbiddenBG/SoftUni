number = int(input())

students = {}

for _ in range(number):
    student, grade = input().split()
    grade = float(grade)
    if student not in students:
        students[student] = []
    students[student].append(grade)

for data in students.items():
    print(f"{data[0]} -> {' '.join([f'{x:.2f}' for x in data[1]])} (avg: {sum(data[1]) / len(data[1]):.2f})")
