numbers = [int(el) for el in input().split()]

command = input()
while not command == "Finish":
    main_data = command.split()
    data = main_data[0]
    if data == "Add":
        value = int(main_data[1])
        numbers.append(value)
    elif data == "Remove":
        value = int(main_data[1])
        if value in numbers:
            numbers.remove(value)
        else:
            continue
    elif data == "Replace":
        value = int(main_data[1])
        replace = int(main_data[2])
        if value in numbers:
            index = numbers.index(value)
            numbers.pop(index)
            numbers.insert(index, replace)
        else:
            continue
    elif data == "Collapse":
        value = int(main_data[1])
        for num in range(len(numbers)):
            if numbers[num] < value:
                numbers[num] = 0
        numbers = [el for el in numbers if el != 0]
    command = input()

print(*numbers, sep=" ")
