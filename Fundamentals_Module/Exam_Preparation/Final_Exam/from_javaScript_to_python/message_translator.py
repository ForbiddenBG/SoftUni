import re

number = int(input())
encrypted = []

for i in range(number):
    text = input()
    pattern = r"(\!)([A-Z][a-z]{2,})+\1\:\[([A-Za-z]{8,})\]"
    valid_message = [el for el in re.finditer(pattern, text)]
    if valid_message:
        for el in valid_message:
            current = el.group(3)
            for letter in current:
                if letter.isalpha():
                    encrypted.append(str(ord(letter)))
            print(f"{el.group(2)}: {' '.join(encrypted)}")
    else:
        print(f"The message is invalid")
