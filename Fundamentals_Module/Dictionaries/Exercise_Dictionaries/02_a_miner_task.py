data = input()

my_dict = {}

while not data == "stop":
    quantity = int(input())
    if data not in my_dict:
        my_dict[data] = quantity
    else:
        my_dict[data] += quantity
    data = input()

for key, value in my_dict.items():
    print(f"{key} -> {value}")