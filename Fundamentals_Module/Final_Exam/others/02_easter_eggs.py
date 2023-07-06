import re

text = input()

pattern = r"(@|#)+([a-z]{3,})(@|#)+(\*|\/|\%|\^|\&|\$)+(\d+)(\/+)"

valid_match = re.finditer(pattern, text)

for el in valid_match:
    print(f"You found {el.group(5)} {el.group(2)} eggs!")
