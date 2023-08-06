import re

information = input()
furniture = []
total_cost = 0
pattern = r">>(?P<name>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)"

while not information == "Purchase":
    match = re.match(pattern, information)
    if match:
        data = match.groupdict()
        furniture.append(data['name'])
        total_cost += float(data['price']) * int(data['quantity'])
    information = input()

print("Bought furniture:")
if furniture:
    print(*furniture, sep='\n')
print(f"Total money spend: {total_cost:.2f}")
