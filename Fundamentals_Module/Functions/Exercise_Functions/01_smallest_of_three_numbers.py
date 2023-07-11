# import sys

# В def за параметър може да се използва *args за всички изброени аргументи.
def smallest_number(some_numbers):
    # min_number = sys.maxsize
    # for number in some_numbers:
    #     if number < min_number:
    #         min_number = number
    return min(some_numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())

numbers = [first_number, second_number, third_number]

# print(min(numbers))

print(smallest_number(numbers))
