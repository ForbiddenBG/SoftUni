vowels = ["a", "e", "o", "i"]
text = input()

print("".join([el for el in text if el.lower not in vowels]))

# result = []
# for el in text:
#     if el.lower() not in vowels:
#         result.append(el)
#
# print("".join(result))
