import re

number = int(input())
numbers = []

for _ in range(number):
    string = input()
    pattern = r"\!(?P<command>[A-Z][a-z]{3,})\!\:\[(?P<name>[A-Za-z][A-Za-z]{7,})\]"
    valid_match = [el.groupdict() for el in re.finditer(pattern, string)]
    if valid_match:
        for el in valid_match:
            for i in el['name']:
                numbers.append(ord(i))
            print(f"{el['command']}: {' '.join([str(el) for el in numbers])}")
    else:
        print("The message is invalid")
