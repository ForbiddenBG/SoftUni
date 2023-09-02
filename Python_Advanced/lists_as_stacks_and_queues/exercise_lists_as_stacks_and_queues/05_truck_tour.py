from collections import deque

number_of_pumps = int(input())
gas_stations = deque()

for _ in range(number_of_pumps):
    pump_info = [int(x) for x in input().split()]
    gas_stations.append(pump_info)

for turn in range(number_of_pumps):
    tank = 0
    failed = False
    for fuel, destination in gas_stations:
        tank += fuel
        if destination > tank:
            failed = True
            break
        else:
            tank -= destination

    if failed:
        gas_stations.append(gas_stations.popleft())
    else:
        print(turn)
        break
