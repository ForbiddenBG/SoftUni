team = input()
souvenirs = input()
souvenirs_count = int(input())

price = 0

if team == "Argentina":
    if souvenirs == "flags":
        price = 3.25 * souvenirs_count
    elif souvenirs == "caps":
        price = 7.20 * souvenirs_count
    elif souvenirs == "posters":
        price = 5.10 * souvenirs_count
    elif souvenirs == "stickers":
        price = 1.25 * souvenirs_count
elif team == "Brazil":
    if souvenirs == "flags":
        price = 4.20 * souvenirs_count
    elif souvenirs == "caps":
        price = 8.50 * souvenirs_count
    elif souvenirs == "posters":
        price = 5.35 * souvenirs_count
    elif souvenirs == "stickers":
        price = 1.20 * souvenirs_count
elif team == "Croatia":
    if souvenirs == "flags":
        price = 2.75 * souvenirs_count
    elif souvenirs == "caps":
        price = 6.90 * souvenirs_count
    elif souvenirs == "posters":
        price = 4.95 * souvenirs_count
    elif souvenirs == "stickers":
        price = 1.10 * souvenirs_count
elif team == "Denmark":
    if souvenirs == "flags":
        price = 3.10 * souvenirs_count
    elif souvenirs == "caps":
        price = 6.50 * souvenirs_count
    elif souvenirs == "posters":
        price = 4.80 * souvenirs_count
    elif souvenirs == "stickers":
        price = 0.90 * souvenirs_count

if team == "Argentina" or team == "Brazil" or team == "Croatia" or team == "Denmark":
    if souvenirs == "flags" or souvenirs == "caps" or souvenirs == "posters" or souvenirs == "stickers":
        print(f"Pepi bought {souvenirs_count} {souvenirs} of {team} for {price:.2f} lv.")
    else:
        print("Invalid stock!")
else:
    print("Invalid country!")
