def best_list_pureness(*args):
    my_list = args[0]
    number = args[1]
    pureness = {}
    rotation = 0
    for _ in range(number+1):
        total = 0
        for idx, value in enumerate(my_list):
            total += value * idx
        pureness[rotation] = total
        my_list.insert(0, my_list.pop())
        rotation += 1

    for k, v in pureness.items():
        if v == max(pureness.values()):
            return f"Best pureness {v} after {k} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
