string = input()

final = ""

for char in string:
    result = ord(char) + 3
    final += chr(result)

print(final)
