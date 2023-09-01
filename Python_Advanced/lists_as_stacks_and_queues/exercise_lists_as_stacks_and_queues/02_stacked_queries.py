my_stack = []

n = int(input())

for _ in range(n):
    main_data = input().split()
    command = main_data[0]
    if main_data[0] == "1":
        my_stack.append(int(main_data[1]))
    elif main_data[0] == "2" and my_stack:
        my_stack.pop()
    elif main_data[0] == "3" and my_stack:
        print(max(my_stack))
    elif main_data[0] == "4" and my_stack:
        print(min(my_stack))

while my_stack:
    element = my_stack.pop()
    if my_stack:
        print(element, end=", ")
    else:
        print(element)
