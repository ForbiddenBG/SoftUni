for num in range(10):
    number = int(input())
    if number % 2 == 0:
        print("Please write an odd number.")
    if number % 2 == 1:
        print(f"The number is: {abs(number)}")
        break
