words = input().split()

my_dict = {}

for el in words:
    el = el.lower()
    if el not in my_dict:
        my_dict[el] = 1
    else:
        my_dict[el] += 1

for key, value in my_dict.items():
    if value % 2 == 1:
        print(key, end=" ")
