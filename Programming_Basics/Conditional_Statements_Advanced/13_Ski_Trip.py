days_of_holiday = int(input())
room_type = input()
feedback = input()
nights = days_of_holiday - 1

price = 0.0

if room_type == "room for one person":
    price = 18
elif room_type == "apartment":
    price = 25
    if days_of_holiday < 10:
        price = price * 0.7
    elif 10 <= days_of_holiday < 15:
        price = price * 0.65
    else:
        price = price * 0.5
elif room_type == "president apartment":
    price = 35
    if nights < 10:
        price = price * 0.9
    elif 10 <= days_of_holiday < 15:
        price = price * 0.85
    else:
        price = price * 0.8

final_price = price * nights
if feedback == "positive":
    final_price = final_price * 1.25
elif feedback == "negative":
    final_price = final_price * 0.9

print(f"{final_price:.2f}")