strings = input().split()
first_string = strings[0]
second_string = strings[1]
difference = abs(len(first_string) - len(second_string))
total_sum = 0

if len(first_string) > len(second_string):
    for index in range(0, len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(first_string) - difference, len(second_string)):
        total_sum += ord(first_string[index])
elif len(second_string) > len(first_string):
    for index in range(0, len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(second_string) - difference, len(second_string)):
        total_sum += ord(second_string[index])
else:
    for index in range(0, len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])

    print(total_sum)

# def first_string_is_greater(str1, str2, total_sum, difference):
#     for index in range(0, len(str2)):
#         total_sum += ord(str1[index]) * ord(str2[index])
#     for index in range(len(str1) - difference, len(str1)):
#         total_sum += ord(str1[index])
#     return total_sum
#
#
# def second_string_is_greater(str2, str1, total_sum, difference):
#     for index in range(0, len(str1)):
#         total_sum += ord(str1[index]) * ord(str2[index])
#     for index in range(len(str2) - difference, len(str2)):
#         total_sum += ord(str2[index])
#     return total_sum
#
#
# def even(str1, str2, total_sum):
#     for index in range(0, len(str1)):
#         total_sum += ord(str1[index]) * ord(str2[index])
#     return total_sum
#
#
# strings = input().split()
# ts = 0
# df = abs(len(strings[0]) - len(strings[1]))
#
# if len(strings[0]) > len(strings[1]):
#     print(first_string_is_greater(strings[0], strings[1], ts, df))
# elif len(strings[1]) > len(strings[0]):
#     print(second_string_is_greater(strings[1], strings[0], ts, df))
# else:
#     print(even(strings[0], strings[1], ts))
