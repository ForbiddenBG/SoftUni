def min_max_sum(nums):
    sum_of_digits = []
    for n in nums:
        sum_of_digits.append(int(n))
    return min(sum_of_digits), max(sum_of_digits), sum(sum_of_digits)


numbers = input().split()
minimum, maximum, sums = min_max_sum(numbers)
print(f"The minimum number is {minimum}")
print(f"The maximum number is {maximum}")
print(f"The sum number is: {sums}")
