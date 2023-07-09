def absolute_value(nums):
    final = []
    for num in range(len(nums)):
        number = float(nums[num])
        number = abs(number)
        final.append(number)
    print(final)


string = input().split()
absolute_value(string)
