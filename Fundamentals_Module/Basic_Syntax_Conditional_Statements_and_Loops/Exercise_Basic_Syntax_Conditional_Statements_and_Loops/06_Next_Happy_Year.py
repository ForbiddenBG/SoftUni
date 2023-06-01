year = int(input())

year += 1

while True:
    year_as_string = str(year)
    if len(year_as_string) == len(set(year_as_string)):
        print(year)
        break
    year += 1

# NB: Infinite Loop Error:
#
# year = int(input()) + 1
#
# while True:
#     is_happy = True
#     year_as_string = str(year)
#     for index_1 in range(len(year_as_string)):
#         for index_2 in range(len(year_as_string)):
#             if index_1 == index_2:
#                 continue
#             if year_as_string[index_1] == year_as_string[index_2]:
#                 is_happy = False
#                 break
#
#     if is_happy:
#         print(year)
#     else:
#         year += 1


# current_year = int(input())
#
# while True:
#     current_year += 1
#     current_year_as_string = str(current_year)
#     if len(current_year_as_string) == len(set(current_year_as_string))
#         print(current_year_as_string)
#         break
