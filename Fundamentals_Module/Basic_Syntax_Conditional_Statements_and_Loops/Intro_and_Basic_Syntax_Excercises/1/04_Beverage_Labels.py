name = input()
volume = int(input())
energy = int(input())
sugar = int(input())

kcal_total = (volume / 100) * energy
sugar_total = (volume / 100) * sugar

print(f"{volume}ml {name}:\n{kcal_total:.2f}kcal, {sugar_total:.2f}g sugars")
