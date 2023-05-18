juniors = int(input())
seniors = int(input())
type_of_road = input()

tax_juniors = 0
tax_seniors = 0
tax_total = 0
max_bikers = juniors + seniors

if type_of_road == "trail":
    tax_juniors = juniors * 5.50
    tax_seniors = seniors * 7
    tax_total = tax_seniors + tax_juniors
elif type_of_road == "downhill":
    tax_juniors = juniors * 12.25
    tax_seniors = seniors * 13.75
    tax_total = tax_seniors + tax_juniors
elif type_of_road == "road":
    tax_juniors = juniors * 20
    tax_seniors = seniors * 21.50
    tax_total = tax_seniors + tax_juniors
elif type_of_road == "cross-country":
    tax_juniors = juniors * 8
    tax_seniors = seniors * 9.50
    tax_total = tax_seniors + tax_juniors
    if type_of_road == "cross-country" and max_bikers >= 50:
        tax_total = (juniors * 8) + (seniors * 9.50)
        tax_total = tax_total - (tax_total * 0.25)

final_price = tax_total - (tax_total * 0.05)

print(f"{final_price:.2f}")
