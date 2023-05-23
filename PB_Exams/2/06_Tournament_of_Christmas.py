number_of_days = int(input())

daily_money = 0
win_counter = 0
lose_counter = 0
total_money = 0
total_win = 0
total_lose = 0

for days in range(1, number_of_days + 1):
    sport = input()
    while sport != "Finish":
        result = input()
        if result == "win":
            daily_money += 20
            win_counter += 1
        else:
            lose_counter += 1
        sport = input()
    if win_counter > lose_counter:
        daily_money = daily_money + (daily_money * 0.1)
    total_money += daily_money
    total_win += win_counter
    total_lose += lose_counter
    daily_money = 0
    win_counter = 0
    lose_counter = 0

if total_win > total_lose:
    total_money = total_money + (total_money * 0.2)
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")



