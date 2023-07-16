words = input().split()
print('\n'.join(s for s in words if len(s) % 2 == 0))

# text = input().split()
# print(*[word for word in text if len(word) % 2 == 0], sep="\n")
