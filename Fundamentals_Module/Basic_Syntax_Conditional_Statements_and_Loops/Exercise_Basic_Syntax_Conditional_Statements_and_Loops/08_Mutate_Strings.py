starting_word = input()
aim_mutated_word = input()

result = ""
previous_str = starting_word

for index in range(len(starting_word)):
    for i in range(index + 1):
        result += aim_mutated_word[i]
    for i in range(index+1, len(aim_mutated_word)):
        result += starting_word[i]
    if not result == previous_str:
        print(result)
    previous_str = result
    result = ""

# first_string = input()
# second_string = input()
#
# last_string = first_string
#
# for symbol_index in range(len(second_string)):
#     left_part = second_string[:symbol_index + 1]
#     right_part = first_string[symbol_index + 1:]
#     current_string = left_part + right_part
#     if current_string == last_string:
#         continue
#     print(current_string)
#     last_string = current_string