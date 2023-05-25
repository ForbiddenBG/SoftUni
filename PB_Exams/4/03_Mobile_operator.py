contract_duration = input()
contract_type = input()
mobile_data = input()
months_to_pay = int(input())

price = 0
if contract_duration == "one":
    if contract_type == "Small":
        price = 9.98
    elif contract_type == "Middle":
        price = 18.99
    elif contract_type == "Large":
        price = 25.98
    elif contract_type == "ExtraLarge":
        price = 35.99
elif contract_duration == "two":
    if contract_type == "Small":
        price = 8.58
    elif contract_type == "Middle":
        price = 17.09
    elif contract_type == "Large":
        price = 23.59
    elif contract_type == "ExtraLarge":
        price = 31.79

if mobile_data == "yes":
    if price <= 10:
        price += 5.5
    elif price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85

if contract_duration == "two":
    price = price * 0.9625  # price - price * 0.0375

total_price = price * months_to_pay
print(f"{total_price:.2f} lv.")