num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

num1 = str(num1)
num2 = str(num2)
num3 = str(num3)
num4 = str(num4)

if len(num1) <= 4:
    new_num = 4 - len(num1)
    print("0" * new_num + num1, end=" ")
if len(num2) <= 4:
    new_num = 4 - len(num2)
    print("0" * new_num + num2, end=" ")
if len(num3) <= 4:
    new_num = 4 - len(num3)
    print("0" * new_num + num3, end=" ")
if len(num4) <= 4:
    new_num = 4 - len(num4)
    print("0" * new_num + num4)
