n = int(input())

evens = []
odds = []
positives = []
negatives = []

for _ in range(n):
    current_number = int(input())

    if current_number % 2 == 0:
        evens.append(current_number)

    if current_number % 2 == 1:
        odds.append(current_number)

    if current_number < 0:
        negatives.append(current_number)

    if current_number > 0:
        positives.append(current_number)

command = input()

if command == "even":
    print(evens)
elif command == "odd":
    print(odds)
elif command == "positive":
    print(positives)
else:
    print(negatives)

# n = int(input())
#
# numbers = []
# filtered = []
#
# for num in range(n):
#     number = int(input())
#     numbers.append(number)
#
# value = input()
# for i in numbers:
#     if value == "even":
#         if i % 2 == 0:
#             filtered.append(i)
#     if value == "odd":
#         if i % 2 == 1:
#             filtered.append(i)
#     if value == "negative":
#         if i < 0:
#             filtered.append(i)
#     if value == "positive":
#         if 0 <= i:
#             filtered.append(i)
#
# print(filtered)
