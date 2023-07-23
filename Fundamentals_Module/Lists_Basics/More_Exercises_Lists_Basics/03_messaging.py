numbers = input().split()
string = input()

current_index = 0
filtered = ""
rest = 0
my_list = list(string)
new_list = []

for char in numbers:
    for sign in char:
        current_index += int(sign)
    if current_index > len(my_list):
        rest = abs(current_index - len(my_list))
        filtered += my_list[rest]
        my_list.remove(my_list[rest])
    else:
        for i in range(len(my_list)):
            if i == current_index:
                filtered += my_list[i]
                my_list.remove(my_list[i])

    new_list = my_list.copy()
    my_list.clear()
    my_list = new_list.copy()
    new_list.clear()
    current_index = 0

print(filtered)
