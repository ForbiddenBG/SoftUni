paper_rolls = int(input())
plat_count = int(input())
glue_liters = float(input())
discount = int(input()) / 100

paper_cost = paper_rolls * 5.80
plat_cost = plat_count * 7.20
glue_cost = glue_liters * 1.20

total = plat_cost + paper_cost + glue_cost
with_dis = total - (total * discount)

print(f"{with_dis:.3f}")
