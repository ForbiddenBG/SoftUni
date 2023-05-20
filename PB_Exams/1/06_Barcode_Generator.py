start_num = int(input())
finish_num = int(input())

current_num = start_num

#while current_num <= finish_num:
barcode = str(current_num)
size = len(barcode)
current_barcode = ""
for i in range(0, size):
    barcode[i] = int(barcode[i])
    if barcode[1] % 2 != 0:
        current_barcode += str(barcode[i])
    else:
        barcode[i] = barcode[i + 1]
        current_barcode += str(barcode[i])




