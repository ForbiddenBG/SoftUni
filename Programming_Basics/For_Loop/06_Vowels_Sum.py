text = input()
sum_voc = 0
for i in range(0, len(text)):
    symbol = text[i]
    if symbol == "a":
        sum_voc = sum_voc + 1
    elif symbol == "e":
        sum_voc = sum_voc + 2
    elif symbol == "i":
        sum_voc = sum_voc + 3
    elif symbol == "o":
        sum_voc = sum_voc + 4
    elif symbol == "u":
        sum_voc = sum_voc + 5
print(sum_voc)
