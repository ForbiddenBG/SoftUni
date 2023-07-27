numbers = input().split()
numbers = [int(el) for el in numbers]

command = input()
while not command == "end":
    main_items = command.split()
    data = main_items[0]
    if data == "swap":
        index1 = int(main_items[1])
        index2 = int(main_items[2])
        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
    elif data == "multiply":
        index1 = int(main_items[1])
        index2 = int(main_items[2])
        new_value = numbers[index1] * numbers[index2]
        numbers[index1] = new_value
    elif data == "decrease":
        numbers = [numbers[n] - 1 for n in range(len(numbers))]
    command = input()

print(*numbers, sep=", ")
