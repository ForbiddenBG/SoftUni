from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = [int(i) for i in input().split()]
making_process = deque(input().split())

total_honey = 0

while working_bees and nectar:
    first_bee = working_bees[0]
    current_nectar = nectar.pop()
    if current_nectar < first_bee:
        continue
    working_bees.popleft()
    first_symbol = making_process.popleft()
    if first_symbol == "+":
        total_honey += abs(first_bee + current_nectar)
    elif first_symbol == "-":
        total_honey += abs(first_bee - current_nectar)
    elif first_symbol == "*":
        total_honey += abs(first_bee * current_nectar)
    elif first_symbol == "/" and current_nectar > 0:
        total_honey += abs(first_bee / current_nectar)

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")

# from collections import deque
#
# working_bees = deque([int(x) for x in input().split()])
# nectar = [int(x) for x in input().split()]
# symbols = deque(x for x in input().split())
#
# honey_made = 0
#
# while working_bees and nectar:
#     first_bee = working_bees[0]
#     last_nectar = nectar[-1]
#
#     if last_nectar >= first_bee:
#         first_symbol = symbols[0].strip(', ')
#
#         if first_symbol in "+":
#             honey_made += abs(first_bee + last_nectar)
#         elif first_symbol in "-":
#             honey_made += abs(first_bee - last_nectar)
#         elif first_symbol in "*":
#             honey_made += abs(first_bee * last_nectar)
#         elif first_symbol in "/" and last_nectar > 0:
#             honey_made += abs(first_bee / last_nectar)
#
#         working_bees.popleft()
#         nectar.pop()
#         symbols.popleft()
#
#     elif last_nectar < first_bee:
#         nectar.pop()
#
# print(f"Total honey made: {honey_made}")
#
# if working_bees:
#     print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
# if nectar:
#     print(f"Nectar left: {', '.join([str(x) for x in nectar])}")
