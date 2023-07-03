import re

number = int(input())

for _ in range(number):
    text = input()
    pattern = r"^(\$|\%)(?P<tag>[A-Z][a-z]{2,})\1(\:\s)(\[)(?P<num1>\d+)(\])(\|)(\[)(?P<num2>\d+)(\])\7(\[)(?P<num3>\d+)(\])\7$"
    valid_message = [el for el in re.finditer(pattern, text)]
    list_one = []
    if valid_message:
        for el in valid_message:
            current = el.groupdict()
            tag = current['tag']
            group1 = chr(int(current['num1']))
            list_one.append(group1)
            group2 = chr(int(current['num2']))
            list_one.append(group2)
            group3 = chr(int(current['num3']))
            list_one.append(group3)

            print(f"{tag}: {''.join(list_one)}")
    else:
        print("Valid message not found!")
