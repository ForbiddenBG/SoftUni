excursion_price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_price = puzzle_count * 2.60
dolls_price = dolls_count * 3
bears_price = bears_count * 4.10
minions_price = minions_count * 8.20
trucks_price = trucks_count * 2

total_price = puzzle_price + dolls_price + bears_price + minions_price + trucks_price
total_count = puzzle_count + dolls_count + bears_count + minions_count + trucks_count

if total_count >= 50:
    total_price = total_price * 0.75

total_price = total_price * 0.9

if total_price >= excursion_price:
    money_left = total_price - excursion_price
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_need = excursion_price - total_price
    print(f"Not enough money! {money_need:.2f} lv needed.")

