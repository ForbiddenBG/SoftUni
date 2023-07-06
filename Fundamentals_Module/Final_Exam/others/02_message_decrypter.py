import re

number = int(input())

for _ in range(number):
    text = input()
    pattern = r"^(\$|\%)([A-Z][a-z]{2,})\1(\:\s)(\[)([0-9]+)(\])(\|)\4([0-9]+)\6\7\4([0-9]+)\6\7$"
    valid_message = re.match(pattern, text)
    if valid_message:
        all_symbols = ""
        all_symbols += chr(int(valid_message.group(5)))
        all_symbols += chr(int(valid_message.group(8)))
        all_symbols += chr(int(valid_message.group(9)))
        print(f"{valid_message.group(2)}: {all_symbols}")
        all_symbols = ""
    else:
        print("Valid message not found!")
