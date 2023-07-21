list_digits = input().split(" ")
number_to_remove = int(input())

current_list = []

for element in range(len(list_digits)):
    current_list.append(int(list_digits[element]))
for i in range(number_to_remove):
    current_list.remove(min(current_list))

print(*current_list, sep=", ")
