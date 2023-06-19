import re

text = input()

patters = r'([#|])(?P<item>[a-zA-Z\s]+)(\1)(?P<date>\d{2}\/\d{2}\/\d{2})(\1)(?P<calories>10000|[0-9]{1,4})(\1)'
total_calories = 0
matches = re.finditer(patters, text)
item_list = []
for match in matches:
    current = match.groupdict()
    item_list.append(current)
    total_calories += int(current['calories'])

days = total_calories // 2000

print(f'You have food to last you for: {days} days!')

for k in item_list:
    print(f"Item: {k['item']}, Best before: {k['date']}, Nutrition: {k['calories']}")
