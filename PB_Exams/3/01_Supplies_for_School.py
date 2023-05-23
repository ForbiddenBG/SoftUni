packages_pens = int(input())
packages_markers = int(input())
liters_soup = float(input())
percent_discount = int(input()) / 100

pens_cost = packages_pens * 5.80
markers_cost = packages_markers * 7.20
soup_cost = liters_soup * 1.20

total_price = pens_cost + markers_cost + soup_cost
discount = total_price * percent_discount
final = total_price - discount

print(f"{final:.3f}")