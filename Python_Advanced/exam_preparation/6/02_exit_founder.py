player_on_move, waiting_player = input().split(", ")

size = 6
matrix = []

for row in range(size):
    matrix.append(input().split())

counter = 0
resting = []

command = input()
while True:
    current_row, current_col = int(command[1]), int(command[4])
    if player_on_move not in resting:
        if matrix[current_row][current_col] == "E":
            print(f"{player_on_move} found the Exit and wins the game!")
            break
        if matrix[current_row][current_col] == "T":
            print(f"{player_on_move} is out of the game! The winner is {waiting_player}.")
            break
        if matrix[current_row][current_col] == "W":
            print(f"{player_on_move} hits a wall and needs to rest.")
            resting.append(player_on_move)
    else:
        resting.remove(player_on_move)
    counter += 1
    player_on_move, waiting_player = waiting_player, player_on_move
    command = input()
