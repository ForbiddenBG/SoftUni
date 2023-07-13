def calc_factorial(num):
    factorial = 1
    for n in range(2, num + 1):
        factorial *= n
    return factorial


def get_factorial_division(f1, f2):
    return f1 / f2


num1 = int(input())
num2 = int(input())
fact1 = calc_factorial(num1)
fact2 = calc_factorial(num2)
result = get_factorial_division(fact1, fact2)
print(f"{result:.2f}")

# def factorial(num1, num2):
#     fact1 = num1
#     fact2 = num2
#
#     for num in range(1, num1):
#         fact1 *= num
#
#     for n in range(1, num2):
#         fact2 *= n
#
#     result = fact1 / fact2
#     print(f"{result:.2f}")
#
#
# number1 = int(input())
# number2 = int(input())
# factorial(number1, number2)
