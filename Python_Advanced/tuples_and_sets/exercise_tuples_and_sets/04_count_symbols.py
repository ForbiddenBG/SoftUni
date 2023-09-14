string = input()

encounters = {}

for el in range(len(string)):
    current_letter = string[el]
    if current_letter not in encounters:
        encounters[current_letter] = 0
    encounters[current_letter] += 1

for key, value in sorted(encounters.items()):
    print(f"{key}: {value} time/s")

# text = input()
#
# occ = {}
#
# for chr in text:
#     if chr not in occ:
#         occ[chr] = 0
#     occ[chr] += 1
#
# for k, v in sorted(occ.items()):
#     print(f"{k}: {v} time/s")
