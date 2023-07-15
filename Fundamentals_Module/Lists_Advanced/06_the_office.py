happiness = [int(el) for el in input().split()]
# happiness_with_map = list(map(lambda el: int(el), input().split()))
factor = int(input())
multiplied_happiness_by_factor = [num * factor for num in happiness]
# multiplied_happiness_by_factor = list(map(lambda num: num* factor, happiness))
avg_happiness = sum(multiplied_happiness_by_factor) / len(multiplied_happiness_by_factor)

# happy_employees = []
# for h in multiplied_happiness_by_factor:
#     if h >= avg_happiness:
#         happy_employees.append(h)

happy_employees = [h for h in multiplied_happiness_by_factor if h > avg_happiness]

# happy_employees = list(filter(lambda h: h > avg_happiness, multiplied_happiness_by_factor))

half_n = len(multiplied_happiness_by_factor) / 2
if len(happy_employees) >= half_n:
    print(f"Score: {len(happy_employees)}/{len(multiplied_happiness_by_factor)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(multiplied_happiness_by_factor)}. Employees are not happy!")
# print(happy_employees)
