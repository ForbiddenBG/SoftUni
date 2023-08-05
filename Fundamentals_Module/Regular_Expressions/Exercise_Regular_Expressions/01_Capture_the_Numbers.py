import re

text_line = input()
pattern = r"\d+"
all_numbers = []

while text_line:
    numbers = re.findall(pattern, text_line)
    all_numbers.extend(numbers)
    text_line = input()

print(*all_numbers)

# import re
#
# pattern = r"\d+"
#
# numbers = input()
# while numbers:
#     if numbers:
#         valid_numbers = re.findall(pattern, numbers)
#         for match in valid_numbers:
#             print(match, end=" ")
#     numbers = input()
