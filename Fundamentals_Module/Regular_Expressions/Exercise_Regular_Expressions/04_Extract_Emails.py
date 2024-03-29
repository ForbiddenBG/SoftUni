import re

text = input()

pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-z]+-?[a-z]+(\.[a-z]+)+"

valids = [el.group for el in re.finditer(pattern, text)]

print(*valids, sep="\n")
