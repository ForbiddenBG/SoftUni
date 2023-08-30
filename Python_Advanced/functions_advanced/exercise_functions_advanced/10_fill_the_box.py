def fill_the_box(height, length, width, *args):
    volume = height * length * width
    cubes_left = 0
    for el in args:
        if el == "Finish":
            break

        if el > volume:
            el -= volume
            cubes_left += el
            volume = 0
        else:
            volume -= el

    if volume > 0:
        return f"There is free space in the box. You could put {volume} more cubes."
    else:
        return f"No more free space! You have {cubes_left} more cubes."

# def fill_the_box(heigh, length, width, *args):
#     size = heigh * length * width
#     for el in args:
#         if el == "Finish":
#             break
#         size -= el
#     if size > 0:
#         return f"There is free space in the box. You could put {size} more cubes."
#     else:
#         return f"No more free space! You have {abs(size)} more cubes."
