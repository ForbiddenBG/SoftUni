from math import pi
figure = input()
if figure == "square":
    side = float(input())
elif figure == "rectangle":
    side_rec_a = float(input())
    side_rec_b = float(input())
elif figure == "circle":
    radius = float(input())
elif figure == "triangle":
    side_lenght = float(input())
    hight_lenght = float(input())

if figure == "square":
    square_area = side * side
    print(f"{square_area:.3f}")
elif figure == "rectangle":
    area_rec = side_rec_a * side_rec_b
    print(f"{area_rec:.3f}")
elif figure == "circle":
    face_of_circle = pi * radius * radius
    print(f"{face_of_circle:.3f}")
elif figure == "triangle":
    face_of_triangle = (side_lenght / 2) * hight_lenght
    print(f"{face_of_triangle:.3f}")
