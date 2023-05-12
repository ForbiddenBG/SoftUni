start_letter = input()
end_letter = input()
not_accepted = input()

start = ord(start_letter)
end = ord(end_letter)
not_acc = ord(not_accepted)
count = 0

for number1 in range(start, end + 1):
    for number2 in range(start, end + 1):
        for number3 in range(start, end + 1):
            new1 = chr(number1)
            new2 = chr(number2)
            new3 = chr(number3)
            if new3 != not_accepted and new1 != not_accepted and new2 != not_accepted:
                print(f"{new1}{new2}{new3}", end=" ")
                count += 1
print(f"{count}", end=" ")



