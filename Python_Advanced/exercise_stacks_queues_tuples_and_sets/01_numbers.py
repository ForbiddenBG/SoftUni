first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

number = int(input())

for _ in range(number):
    main_data = input().split()
    if main_data[0] == "Add":
        if main_data[1] == "First":
            [first.add(int(x)) for x in main_data[2:]]
        else:
            [second.add(int(x)) for x in main_data[2:]]
    elif main_data[0] == "Remove":
        if main_data[1] == "First":
            [first.discard(int(x)) for x in main_data[2:]]
        else:
            [second.discard(int(x)) for x in main_data[2:]]
    else:
        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
