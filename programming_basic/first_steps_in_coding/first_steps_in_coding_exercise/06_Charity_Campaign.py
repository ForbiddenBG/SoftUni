days_count = int(input())
bakers_count = int(input())
cakes_count = int(input())
waffles_count = int(input())
crepes_count = int(input())

cake_price = 45
waffles_price = 5.80
crepes_price = 3.20

daily_total = (cake_price * cakes_count + waffles_price * waffles_count + crepes_price * crepes_count) * bakers_count
total = daily_total * days_count

profit = total - (total / 8)
print(profit)