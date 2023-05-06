budget = float(input())
season = input()

destination = ""
type = ""
money = 0.0
if 0 < budget <= 100:
    destination = "Bulgaria"
elif 100 < budget <= 1000:
    destination = "Balkans"
else:
    destination = "Europe"

if destination != "Europe":
    if season == "summer":
        type = "Camp"
    elif season == "winter":
        type = "Hotel"
else:
    type = "Hotel"

if destination == "Bulgaria":
    if season == "summer":
        money = budget - (budget * 0.30)
    elif season == "winter":
        money = budget - (budget * 0.70)
elif destination == "Balkans":
    if season == "summer":
        money = budget - (budget * 0.40)
    elif season == "winter":
        money = budget - (budget * 0.80)
elif destination == "Europe":
    money = budget - (budget * 0.90)

money_needed = budget - money
print(f"Somewhere in {destination}")
print(f"{type} - {money_needed:.2f}")