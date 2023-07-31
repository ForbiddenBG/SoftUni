waiting_list = int(input())
current_state = [int(element) for element in input().split()]
max_capacity = len(current_state) * 4
capacity = sum(current_state)
for ride in range(len(current_state)):
    while current_state[ride] < 4 and waiting_list > 0:
        current_state[ride] += 1
        waiting_list -= 1
        capacity += 1
capacity += waiting_list
if waiting_list > 0:
    print(f"There isn't enough space! {waiting_list} people in a queue!")
elif capacity < max_capacity:
    print("The lift has empty spots!")
print(' '.join([str(element) for element in current_state]))
