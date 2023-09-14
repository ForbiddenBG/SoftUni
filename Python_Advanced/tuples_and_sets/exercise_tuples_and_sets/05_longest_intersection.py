def gen_seq(range_info):
    start, end = [int(x) for x in range_info.split(',')]
    return set(range(start, end+1))


number = int(input())

best_intersection = set()

for _ in range(number):
    parts = input().split("-")
    first_set = gen_seq(parts[0])
    second_set = gen_seq(parts[1])
    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(best_intersection):
        best_intersection = current_intersection

print(
    f"Longest intersection is [{', '.join([str(x) for x in best_intersection])}] with length {len(best_intersection)}")
