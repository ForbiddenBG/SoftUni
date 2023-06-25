import re

text = input()

digits = r"\d"
pattern = r"(\:|\*){2}[A-Z][a-z]{2,}\1{2}"

cool_treshold = 1
coolness = 0
valid_digits = re.findall(digits, text)
valid_emojis = re.finditer(pattern, text)
count = 0
emojis = []

for el in valid_digits:
    cool_treshold *= int(el)

for match in valid_emojis:
    current = match.group()
    emoji_without_surrondings = current[2:-2]
    coolness = sum([ord(el) for el in emoji_without_surrondings])
    if cool_treshold <= coolness:
        emojis.append(current)
    count += 1

print(f"Cool threshold: {cool_treshold}")
print(f"{count} emojis found in the text. The cool ones are:")
for el in emojis:
    print("".join(el))
