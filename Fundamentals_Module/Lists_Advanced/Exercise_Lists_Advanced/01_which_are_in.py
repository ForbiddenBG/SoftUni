substrings = input().split(", ")
words = input().split(", ")

occ_substrings = [substr for substr in substrings for word in words if substr in word]

print(sorted(set(occ_substrings), key=occ_substrings.index))

# words = input().split(", ")
# sequence = input().split(", ")
#
# my_list = []
#
# for word in words:
#     for s in sequence:
#         if word in s and word not in my_list:
#             my_list.append(word)
#
# print(my_list)
