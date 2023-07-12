def is_even(number):
    if number % 2 == 0:
        return True
    return False


numbers = input().split()
filtered_numbers = []
for number in numbers:
    if is_even(int(number)):       # if is_even(int(number)) == True
        filtered_numbers.append(int(number))

print(filtered_numbers)

# numbers = input().split()
#
# numbers_as_digits = []
#
# for number in numbers:
#     numbers_as_digits.append(int(number))
#
# is_even = lambda x: x % 2 == 0
# result = list(filter(is_even, numbers_as_digits))
#
# print(result)
