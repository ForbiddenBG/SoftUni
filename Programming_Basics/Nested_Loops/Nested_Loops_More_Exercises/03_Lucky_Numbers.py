number = int(input())

for number1 in range(1, 9 + 1):
    for number2 in range(1, 9 + 1):
        for number3 in range(1, 9 + 1):
            for number4 in range(1, 9 + 1):
                sum1 = number1 + number2
                sum2 = number3 + number4
                if sum1 == sum2 and number % sum1 == 0:
                    print(f"{number1}{number2}{number3}{number4}", end=" ")
                    continue





