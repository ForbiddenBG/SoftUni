numbers_as_strings = input().split()
numbers_desc_as_string = sorted(numbers_as_strings, reverse=True)
print("".join(numbers_desc_as_string))
