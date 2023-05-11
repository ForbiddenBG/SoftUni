n = int(input())
l = int(input())

for first_char in range(1, n + 1):
    for second_char in range(1, n + 1):
        for third_char in range(ord("a"), ord("a") + l):
            for fourth_char in range(ord("a"), ord("a") + l):
                for fifth_char in range(1, n + 1):
                    if first_char < fifth_char > second_char:
                        print(f"{first_char}{second_char}{chr(third_char)}{chr(fourth_char)}{fifth_char}", end=" ")
