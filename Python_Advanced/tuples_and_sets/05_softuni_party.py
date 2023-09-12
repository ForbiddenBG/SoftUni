number = int(input())

guests = set()

for _ in range(number):
    guests.add(input())

command = input()
while not command == "END":
    guests.discard(command)
    command = input()

print(len(guests))
print('\n'.join(sorted(guests)))
