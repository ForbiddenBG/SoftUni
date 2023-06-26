import re

number = int(input())

for _ in range(number):
    main_data = input()
    pattern = r"(?<=\|)(?P<name>([A-Z]{4,}))(?P<separator>\|\:\#)(?P<title>([A-Za-z]+)\s([A-Za-z]+))(?=\#)"
    valid_groups = [el.groupdict() for el in re.finditer(pattern, main_data)]
    if valid_groups:
        for item in valid_groups:
            print(f"{item['name']}, The {item['title']}")
            print(f">> Strength: {len(item['name'])}")
            print(f">> Armour: {len(item['title'])}")
    else:
        print("Access denied!")
