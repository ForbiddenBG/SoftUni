import re

text = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

valid_numbers = [matched_obj.group() for matched_obj in re.finditer(pattern, text)]
print(*valid_numbers)
