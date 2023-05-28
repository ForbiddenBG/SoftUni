string = input()
string_in_lower_case = string.lower()
count_sun = string_in_lower_case.count('sun')
count_water = string_in_lower_case.count('water')
count_sand = string_in_lower_case.count('sand')
count_fish = string_in_lower_case.count('fish')
total_count = count_fish + count_sand + count_sun + count_water
print(total_count)
