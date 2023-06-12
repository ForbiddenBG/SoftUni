lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

sum_for_repair = 0
broken_shield_count = 0

for lost_fight in range(1, lost_fights_count + 1):
    if lost_fight % 2 == 0:
        sum_for_repair += helmet_price

    if lost_fight % 3 == 0:
        sum_for_repair += sword_price

    if lost_fight % 2 == 0 and lost_fight % 3 == 0:
        sum_for_repair += shield_price
        broken_shield_count += 1

        if broken_shield_count % 2 == 0 and not broken_shield_count == 0:
            sum_for_repair += armor_price

print(f"Gladiator expenses: {sum_for_repair:.2f} aureus")

# lost_fights = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
#
# expenses = 0
#
# for fight in range(1, lost_fights + 1):
#     if fight % 2 == 0:
#         expenses += helmet_price
#     if fight % 3 == 0:
#         expenses += sword_price
#     if fight % 6 == 0:
#         expenses += shield_price
#         if fight % 12 == 0:
#             expenses += armor_price
#
# print(f"Gladiator expenses: {expenses:.2f} aureus")
