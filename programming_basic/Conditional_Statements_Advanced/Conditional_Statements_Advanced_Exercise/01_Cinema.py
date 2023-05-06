screening_type = input()
rows = int(input())
cols = int(input())

income = 0

if screening_type == "Premiere":
    income = rows * cols * 12
elif screening_type == "Normal":
    income = rows * cols * 7.5
elif screening_type == "Discount":
    income = rows * cols * 5

print(f"{income:.2f} leva")