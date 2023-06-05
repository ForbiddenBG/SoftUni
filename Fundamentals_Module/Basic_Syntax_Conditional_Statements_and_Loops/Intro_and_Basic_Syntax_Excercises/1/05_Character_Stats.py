name = input()
current_health = int(input())
maximum_health = int(input())
current_energy = int(input())
maximum_energy = int(input())

point = "|"
miss = "."
health_missing = maximum_health - current_health
energy_missing = maximum_energy - current_energy

print(f"Name: {name}\n"
      f"Health: |{point * current_health}{miss * health_missing}|\n"
      f"Energy: |{point * current_energy}{miss * energy_missing}|")
