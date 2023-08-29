def even_odd(*args):
    command = args[-1]
    parity = 0 if command == "even" else 1
    return [x for x in args[:len(args) - 1] if x % 2 == parity]

# def even_odd(*args):
#     command = args[-1]
#     parity = 0 if command == "even" else 1
#     return [x for x in args[:-1] if x % 2 == parity]

# def even_odd(*args):
#     command = args[-1]
#     my_list = []
#     for el in args[:-1]:
#         if command == "even":
#             if el % 2 == 0:
#                 my_list.append(el)
#         else:
#             if el % 2 == 1:
#                 my_list.append(el)
#     return my_list
