import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
text = input()
# names = input().split(", ")
valid_names = re.findall(pattern, text)
print(" ".join(valid_names))
# valid_names = []

# for name in names:
#     match = re.match(pattern, name)
#     if match:
#         print(match.group())
#         valid_names.append(match.group())
#
# print(" ".join(valid_names))
