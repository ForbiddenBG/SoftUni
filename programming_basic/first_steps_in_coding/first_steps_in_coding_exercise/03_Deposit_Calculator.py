deposit = float(input())
time_of_deposit = int(input())
percent_for_year = float(input())

interest = (deposit * (percent_for_year / 100))
interest_per_month = interest / 12


final_money = deposit + time_of_deposit * interest_per_month

print(final_money)