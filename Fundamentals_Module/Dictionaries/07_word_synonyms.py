n = int(input())

synonyms = {}

for _ in range(n):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for key, values in synonyms.items():
    print(f"{key} - {', '.join(values)}")
