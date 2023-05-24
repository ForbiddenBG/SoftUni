groups_count = int(input())

destination = ""
percent_Musala = 0
percent_Monblan = 0
percent_Kilimangaroo = 0
percent_K2 = 0
percent_Everest = 0
num = 0

while num != groups_count:
    ppl_count_in_the_group = int(input())
    for person in range(1, ppl_count_in_the_group + 1):
        if ppl_count_in_the_group <= 5:
            destination = "Musala"
            percent_Musala = ppl_count_in_the_group / 100
        elif 6 <= ppl_count_in_the_group <= 12:
            destination = "Monblan"
            percent_Monblan = ppl_count_in_the_group / 100
        elif 13 <= ppl_count_in_the_group <= 25:
            destination = "Kilimangaroo"
            percent_Kilimangaroo = ppl_count_in_the_group / 100
        elif 26 <= ppl_count_in_the_group <= 40:
            destination = "K2"
            percent_K2 = ppl_count_in_the_group / 100
        elif 41 <= ppl_count_in_the_group:
            destination = "Everest"
            percent_Everest = ppl_count_in_the_group / 100
        ppl_count_in_the_group = int(input())
    num += 1
    groups_count = int(input())

print(f"{percent_Musala:.2f}%")
print(f"{percent_Monblan:.2f}%")
print(f"{percent_Kilimangaroo:.2f}%")
print(f"{percent_K2:.2f}%")
print(f"{percent_Everest:.2f}%")