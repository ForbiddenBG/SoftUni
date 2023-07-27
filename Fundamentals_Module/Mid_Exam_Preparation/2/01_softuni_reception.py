students_per_employee_No1 = int(input())
students_per_employee_No2 = int(input())
students_per_employee_No3 = int(input())
students_count = int(input())

hour = 0

while students_count > 0:
    hour += 1
    if not hour % 4 == 0:
        students_count -= students_per_employee_No1
        students_count -= students_per_employee_No2
        students_count -= students_per_employee_No3

print(f"Time needed: {hour}h.")
