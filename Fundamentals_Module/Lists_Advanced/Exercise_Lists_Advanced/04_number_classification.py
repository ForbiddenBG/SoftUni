def positive_numbers(numbers):
    return [str(number) for number in numbers if number >= 0]
def negative_numbers(numbers):
    return [str(number) for number in numbers if number < 0]
def even_numbers(numbers):
    return [str(number) for number in numbers if number % 2 == 0]
def odd_numbers(numbers):
    return [str(number) for number in numbers if number % 2 == 1]


numbers = [int(s) for s in input().split(", ")]

print(f"Positive: {', '.join(positive_numbers(numbers))}")
print(f"Negative: {', '.join(negative_numbers(numbers))}")
print(f"Even: {', '.join(even_numbers(numbers))}")
print(f"Odd: {', '.join(odd_numbers(numbers))}")

# numbers = input().split(", ")
#
# print(f"Positive: {', '.join([number for number in numbers if int(number) >= 0])}")
# print(f"Negative: {', '.join([number for number in numbers if int(number) < 0])}")
# print(f"Even: {', '.join([number for number in numbers if int(number) % 2 == 0])}")
# print(f"Odd: {', '.join([number for number in numbers if int(number) % 2 == 1])}")


