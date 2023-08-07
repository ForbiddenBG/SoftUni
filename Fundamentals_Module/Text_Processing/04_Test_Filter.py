banned_words = input().split(", ")
text = input()

for word in banned_words:
    text = text.replace((banned_words, "*" * len(word)))

print(text)
