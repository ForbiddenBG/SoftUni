word = input()

while not word == "end":
    print(f"{word} = {word[::-1]}")
    word = input()

# word = input()
# result = ""
#
# while not word == "end":
#     for char in reversed(word):
#         result += char
#     print(f"{word} = {result}")
#     result = ""
#     word = input()
