string = input()

string_to_list = list(string)
new_list = []

for index in range(len(string)):
    if string[index].isupper():
        new_list.append(index)

print(new_list)
