import re

number = int(input())
new_string = ""

for _ in range(number):
    text = input()
    pattern = r"(.+)>(?P<gr1>[0-9]+)\|(?P<gr2>[a-z]+)\|(?P<gr3>[A-Z]+)\|(?P<gr4>[a-zA-Z0-9@!#\*]+)<\1"
    valid_match = [el.groupdict() for el in re.finditer(pattern, text)]
    if valid_match:
        new_string += valid_match[0]['gr1']
        new_string += valid_match[0]['gr2']
        new_string += valid_match[0]['gr3']
        new_string += valid_match[0]['gr4']
        print(f"Password: {new_string}")
    else:
        print("Try another password!")
    new_string = ""
