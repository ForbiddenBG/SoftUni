string = input().split("|")

result = []

while string:
    substring = string.pop()
    result.extend(substring.split())

print(*result)


# sublists = input().split("|")
#
# result = []
# while sublists:
#     sublist = sublists.pop().split()
#     for el in sublist:
#         result.append(el)
#
# print(*result, sep=" ")


# sublists = input().split("|")
#
# while sublists:
#     sublist = sublists.pop().split()
#     if sublist:
#         print(" ".join(sublist), end=" ")
