from itertools import permutations


def possible_permutations(elements):
    result = permutations(elements)

    for perm in result:
        yield list(perm)

# def permute(idx, elements):
#     if idx >= len(elements):
#         print(elements)
#         return
#
#     permute(idx + 1, elements)
#
#     for i in range(idx + 1, len(elements)):
#         elements[idx], elements[i] = elements[i], elements[idx]
#         permute(idx + i, elements)
#         elements[idx], elements[i] = elements[i], elements[idx]
#
#
# elements = ["A", "B", "C"]
# permute(0, elements)