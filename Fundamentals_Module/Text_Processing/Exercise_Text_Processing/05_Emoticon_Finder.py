text = input()

# emojis = [f"{text[index]}{text[index + 1]}" for index in range(0, len(text)) if text[index] == ":"]
#
# print("\n".join(emojis))

emojis = []

for index in range(0, len(text)):
    if text[index] == ":":
        emojis.append(f"{text[index]}{text[index + 1]}")

print("\n".join(emojis))

# string = input()
# result = ""
#
# for char in range(len(string)):
#     if string[char] == ":":
#         result += string[char] + string[char + 1]
#         print(result)
#     result = ""
