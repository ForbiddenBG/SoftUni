def sorting_numbers(list_of_numbers):
    return sorted(list_of_numbers)


numbers = input().split()
numbers_as_digits = []
for number in numbers:
    numbers_as_digits.append(int(number))
sorted_numbers = sorting_numbers(numbers_as_digits)
print(sorted_numbers)

# def sorted_nums(nums):
#     my_list = []
#     for number in nums:
#         numb = int(number)
#         my_list.append(numb)
#     return sorted(my_list)
#
#
# numbers = input().split()
#
# print(sorted_nums(numbers))

# numbers = input().split()
# my_list = []
# for number in numbers:
#     numb = int(number)
#     my_list.append(numb)
# print(sorted(my_list))
