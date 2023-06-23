import re

text = input()
valids = []
counter = 0

pattern = r"(@|#)(?P<word_1>[a-zA-Z]{3,})\1\1(?P<word_2>[a-zA-Z]{3,})\1"

words = re.finditer(pattern, text)

for word in words:
    current = word.groupdict()
    if current['word_1'] == current['word_2'][::-1]:
        valids.append(f"{current['word_1']} <=> {current['word_2']}")
    counter += 1

if counter == 0:
    print("No word pairs found!")
else:
    print(f"{counter} word pairs found!")

if valids:
    print("The mirror words are:")
    print(", ".join(valids))
else:
    print("No mirror words!")