money_for_day = float(input())
earnings_for_day = float(input())
total_expences = float(input())
present_cost = float(input())

money_for_days = money_for_day * 5
for_all_days = earnings_for_day * 5

total = (money_for_days + for_all_days) - total_expences



if total > present_cost:
    print(f"Profit: {total:.2f} BGN, the gift has been purchased.")
else:
    not_enough = total - present_cost
    print(f"Insufficient money: {abs(not_enough):.2f} BGN.")