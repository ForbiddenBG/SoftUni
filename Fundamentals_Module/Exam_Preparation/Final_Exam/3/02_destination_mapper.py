import re

string = input()

pattern = r"(\=|\/)([A-Z]{1}[a-zA-Z]+[a-zA-Z])\1"
total_points = 0
destinations = []

valid_matches = re.finditer(pattern, string)

for el in valid_matches:
    current = el.group().strip('=/')
    total_points += len(current)
    destinations.append(current)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {total_points}")

# import re
#
# text = input()
# total_sum = 0
# destination = []
#
# pattern = r"(\=|\/)([A-Z]{1}[a-zA-Z]{2,})\1"
#
# valid_destinations = re.finditer(pattern, text)
#
# for el in valid_destinations:
#     current = el.group(2)
#     destination.append(current)
#     total_sum += len(current)
#
# print(f"Destinations: {', '.join(destination)}")
# print(f"Travel Points: {total_sum}")
