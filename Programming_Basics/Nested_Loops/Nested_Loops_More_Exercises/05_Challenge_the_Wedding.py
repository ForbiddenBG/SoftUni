men_count = int(input())
women_count = int(input())
max_table_count = int(input())

ticket_man = 0
ticket_woman = 0
table_counter = 0
flag = False
# total_people = men_count + women_count
total_people = 0
for man in range(1, men_count + 1):

    # ticket_man += 1
    for woman in range(1, women_count + 1):
        total_people += 1
        # ticket_woman += 1
        print(f"({man} <-> {woman})", end=" ")
        if ticket_man + ticket_woman == 2:
            total_people += 1
        #     table_counter += 1
        if total_people / 2 == table_counter:
            flag = True
            break
    if flag:
        break








