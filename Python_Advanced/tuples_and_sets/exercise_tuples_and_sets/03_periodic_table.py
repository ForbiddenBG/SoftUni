number = int(input())

elements = set()

for _ in range(number):
    element = input().split()
    elements = elements.union(element)

print(*elements, sep='\n')

# number = int(input())
#
# chemicals = set()
#
# for _ in range(number):
#     main_chems = input().split()
#     for el in main_chems:
#         chemicals.add(el)
#
# print(*chemicals, sep='\n')

# number = int(input())
#
# my_list = []
# table = set()
#
# for _ in range(number):
#     elements = input().split()
#     my_list.extend(elements)
#
# for el in range(len(my_list)):
#     table.add(my_list[el])
#
# print(*table, sep='\n')
