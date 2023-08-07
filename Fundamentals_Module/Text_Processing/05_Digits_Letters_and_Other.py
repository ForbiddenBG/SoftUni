numbers = ""
letters = ""
characters = ""

text = input()

for char in text:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        letters += char
    else:
        characters += char

print(numbers)
print(letters)
print(characters)
