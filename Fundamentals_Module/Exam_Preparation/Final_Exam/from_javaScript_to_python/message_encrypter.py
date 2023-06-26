import re

number = int(input())

for _ in range(number):
    text = input()
    pattern = r"(\*|@)(?P<tag>[A-Z][a-z]{2,})\1\:\s\[(?P<gr1>[a-zA-Z])\]\|\[(?P<gr2>[a-zA-Z])\]\|\[(?P<gr3>[a-zA-Z])\]\|(?=\s|$)"
    valid_match = [el.groupdict() for el in re.finditer(pattern, text)]
    if valid_match:
        num1 = ord(valid_match[0]['gr1'])
        num2 = ord(valid_match[0]['gr2'])
        num3 = ord(valid_match[0]['gr3'])
        print(f"{valid_match[0]['tag']}: {num1} {num2} {num3}")
    else:
        print("Valid message not found!")
