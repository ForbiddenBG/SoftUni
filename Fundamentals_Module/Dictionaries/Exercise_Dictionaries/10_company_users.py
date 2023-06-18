data = input()

my_dict = {}

while not data == "End":
    company, id = data.split("->")
    if company not in my_dict:
        my_dict[company] = []
        my_dict[company].append(id)
    if id not in my_dict[company]:
        my_dict[company].append(id)
    data = input()

sorted_companies = sorted(my_dict.items(), key=lambda kvp: kvp[0])

for k, v in sorted_companies:
    print(f"{k}")
    for value in v:
        print(f"--{''.join(value)}")
