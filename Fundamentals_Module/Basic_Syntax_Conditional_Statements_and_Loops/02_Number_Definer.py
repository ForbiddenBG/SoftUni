x = float(input())

if x == 0:
    print("zero")
elif x > 0:
    if x < 1:
        print("small positive")
    elif x > 1000000:
        print("large positive")
    else:
        print("positive")
else:
    if abs(x) < 1:
        print("small negative")
    elif abs(x) > 1000000:
        print("large negative")
    else:
        print("negative")
