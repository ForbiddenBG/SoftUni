nums = [int(el) for el in input().split(", ")]
# nums = list(map(lambda x: int(x), input(.split(", "))))

group = 10
max_number = max(nums)

while len(nums) > 0:
    nums_group = []

    for num in nums:
        if num in range(group - 10, group + 1):
            nums_group.append(num)

    for num in nums_group:
        nums.remove(num)

    print(f"Group of {group}'s: {nums_group}")
    group += 10
