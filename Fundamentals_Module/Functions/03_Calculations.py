def calculate(act, num1, num2):
    if act == "multiply":
        return num1 * num2
    elif act == "add":
        return num1 + num2
    elif act == "subtract":
        return num1 - num2
    elif act == "divide":
        return num1 // num2


action = input()
first_num = int(input())
second_num = int(input())
result = calculate(action, first_num, second_num)
print(result)
