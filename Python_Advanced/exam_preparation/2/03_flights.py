def flights(*args):
    destionations = {}
    for idx in range(0, len(args)+1, 2):
        if args[idx] == "Finish":
            return destionations
        if args[idx] not in destionations:
            destionations[args[idx]] = 0
        destionations[args[idx]] += args[idx+1]

# def flights(*args):
#     destinations = {}
#     for el in range(0, len(args)+1, 2):
#         if args[el] != "Finish":
#             word = args[el]
#             value = int(args[el + 1])
#             if word not in destinations:
#                 destinations[word] = value
#             destinations[word] += value
#         else:
#             return destinations


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
