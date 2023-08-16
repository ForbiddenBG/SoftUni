jobs = [int(x) for x in input().split(", ")]
index = int(input())

tasks = {}
clock = 0

for idx, value in enumerate(jobs):
    if idx not in tasks:
        tasks[idx] = value

for k, v in sorted(tasks.items(), key=lambda x: x[1]):
    if k == index:
        clock += v
        break
    else:
        clock += v

print(clock)
