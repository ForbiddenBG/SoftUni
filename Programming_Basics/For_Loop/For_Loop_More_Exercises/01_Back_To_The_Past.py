inherited_money = float(input())
year_life = int(input())

total_money = float(inherited_money)
age = 18

for year in range(1800, year_life + 1):
    if year % 2 == 0:
        total_money -= 12000
    else:
        total_money -= 12000 + 50 * age
    if year_life == True:
        break
    age += 1

if total_money >= 0:
    print(f"Yes! He will live a carefree life and will have {total_money:.2f} dollars left." )
else:
    print(f"He will need {abs(total_money):.2f} dollars to survive.")