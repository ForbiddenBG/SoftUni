def rounding(nums):
    rounds = []
    for num in range(len(nums)):
        number = float(nums[num])
        number = round(number)
        rounds.append(number)
    print(rounds)


numbers = input().split()
rounding(numbers)
