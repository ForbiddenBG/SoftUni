number = int(input())

odd = set()
even = set()

for i in range(1, number + 1):
    name = input()
    sum_of_values = 0
    for el in range(len(name)):
        sum_of_values += ord(name[el])
    sum_of_values //= i
    if sum_of_values % 2 == 0:
        even.add(sum_of_values)
    else:
        odd.add(sum_of_values)

if sum(even) == sum(odd):
    print(f"{', '.join(str(x) for x in even.union(odd))}")
elif sum(odd) > sum(even):
    print(f"{', '.join(str(x) for x in odd.difference(even))}")
elif sum(even) > sum(odd):
    print(f"{', '.join(str(x) for x in even.symmetric_difference(odd))}")

# n = int(input())
#
# odd_sum = set()
# even_sum = set()
#
# for row in range(1, n + 1):
#     name_sum = sum([ord(x) for x in input()]) // row
#     if name_sum % 2 == 0:
#         even.add(name_sum)
#         even_sum += name_sum
#     else:
#         odd.add(name_sum)
#         odd_sum += name_sum
#
# if even_sum == odd_sum:
#     result = odd.union(even)
# elif even_sum > odd_sum:
#     result = odd.symmetric_difference(even)
# else:
#     result = odd.difference(even)
#
# print(*result, sep=", ")

# number = int(input())
#
# odd = set()
# even = set()
#
# for row in range(1, number+1):
#     generator = sum([ord(x) for x in input()]) // row
#     if generator % 2 == 0:
#         even.add(generator)
#     else:
#         odd.add(generator)
#
# sum_odd = sum(odd)
# sum_even = sum(even)
#
# if sum_odd == sum_even:
#     print(*odd.union(even), sep=', ')
# elif sum_odd > sum_even:
#     print(*odd.difference(even), sep=', ')
# elif sum_even > sum_odd:
#     print(*even.symmetric_difference(odd), sep=', ')
