string = input().split(", ")

zeros = []
others = []

for number in string:
    number_as_int = int(number)
    if number_as_int == 0:
        zeros.append(number_as_int)
    else:
        others.append(number_as_int)

print(others + zeros)
