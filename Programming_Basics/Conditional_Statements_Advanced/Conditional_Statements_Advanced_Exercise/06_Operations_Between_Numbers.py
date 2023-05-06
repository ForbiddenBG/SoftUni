n1 = int(input())
n2 = int(input())
operator = input()

result = 0
rest = 0
even_or_odd = ""

if operator == "+":
    result = n1 + n2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
elif operator == "-":
    result = n1 - n2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
elif operator == "*":
    result = n1 * n2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    elif n2 != 0:
        result = n1 / n2
elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    elif n2 != 0:
        rest = n1 % n2


if operator == "+" or operator == "-" or operator == "*":
    print(f"{n1} {operator} {n2} = {result} - {even_or_odd}")
elif operator == "/" and n2 != 0:
    print(f"{n1} / {n2} = {result:.2f}")
elif operator == "%" and n2 != 0:
    print(f"{n1} % {n2} = {rest}")
