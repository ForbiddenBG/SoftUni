text = input()
filtered_letters = ""
last_letter = ""

for current_letter in text:
    if current_letter != last_letter:
        filtered_letters += current_letter
        last_letter = current_letter
print(filtered_letters)

# data = input()
#
# index = 0
#
# while index < len(data) - 1:
#     if data[index] == data[index + 1]:
#         element_to_replace = f"{data[index]}{data[index + 1]}"
#         data = data.replace(element_to_replace, data[index])
#         index = 0
#     else:
#         index += 1
#
# print(data)
