budget = int(input())
season = input()
number_fishermen = int(input())

rent = 0

if season == "Spring" and 0 < number_fishermen <= 6:
    rent = 3000 - (3000 * 0.1)
elif season == "Spring" and 7 <= number_fishermen <= 11:
    rent = 3000 - (3000 * 0.15)
elif season == "Spring" and number_fishermen >= 12:
    rent = 3000 - (3000 * 0.25)

if (season == "Summer" or season == "Autumn") and 0 < number_fishermen <= 6:
    rent = 4200 - (4200 * 0.1)
elif (season == "Summer" or season == "Autumn") and 7 <= number_fishermen <= 11:
    rent = 4200 - (4200 * 0.15)
elif (season == "Summer" or season == "Autumn") and number_fishermen >= 12:
    rent = 4200 - (4200 * 0.25)

if season == "Winter" and 0 < number_fishermen <= 6:
    rent = 2600 - (2600 * 0.1)
elif season == "Winter" and 7 <= number_fishermen <= 11:
    rent = 2600 - (2600 * 0.15)
elif season == "Winter" and number_fishermen >= 12:
    rent = 2600 - (2600 * 0.25)

if number_fishermen % 2 == 0 and (season == "Spring" or season == "Summer" or season == "Winter"):
    rent = rent - (rent * 0.05)

final_money = budget - rent

if budget >= rent:
    print(f"Yes! You have {final_money:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(final_money):.2f} leva.")

