name = input()
age = int(input())
identification = int(input())
salary = float(input())

ide = 8
identification = str(identification)
if ide > len(identification):
    rest = ide - len(identification)
    identification = "0" * rest + identification

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Employee ID: {identification}")
print(f"Salary: {salary:.2f}")
