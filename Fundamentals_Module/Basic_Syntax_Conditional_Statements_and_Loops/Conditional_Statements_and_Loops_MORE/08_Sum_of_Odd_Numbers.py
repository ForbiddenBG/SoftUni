odd_num = int(input())

counter = 0
sum_odds = 0
odds_count = 0

while True:
    counter += 1
    if counter % 2 == 1:
        odds_count += 1
        sum_odds += counter
        print(counter)
        if odd_num == odds_count:
            break

print(f"Sum: {sum_odds}")
