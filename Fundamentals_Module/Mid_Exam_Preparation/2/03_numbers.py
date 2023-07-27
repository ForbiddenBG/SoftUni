numbers = [int(el) for el in input().split()]

max_nums = []
avg_num = sum(numbers) / len(numbers)

for num in range(len(numbers)-1, -1, -1):
    if avg_num < numbers[num]:
        max_nums.append(numbers[num])

max_nums = sorted(max_nums, reverse=True)
if not len(max_nums) == 0:
    print(*max_nums[:5])
else:
    print("No")
