from collections import deque

vowels = deque([x for x in input().split()])
consonants = [x for x in input().split()]

flowers = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil"
}

is_found = False

while vowels and consonants:
    first_vowel = vowels.popleft()
    last_consonant = consonants.pop()
    for k, v in flowers.items():
        if first_vowel in v:
            flowers[k] = flowers[k].replace(first_vowel, "")
        if last_consonant in v:
            flowers[k] = flowers[k].replace(last_consonant, "")
        if flowers[k] == "":
            print(f"Word found: {k}")
            is_found = True
            break
    if is_found:
        break

if not is_found:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join([x for x in vowels])}")
if consonants:
    print(f"Consonants left: {' '.join([x for x in consonants])}")
