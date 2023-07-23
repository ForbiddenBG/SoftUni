string = input().split()

largest_num = []
largest_as_string = ""

for large in range(len(string)):
    largest_num.append(max(string))
    string.remove(max(string))

for num in largest_num:
    largest_as_string += num

print(largest_as_string)

# numbers = input().split()
# for i in range(len(numbers)):
#     print(max(numbers), end="")
#     numbers.remove(max(numbers))
