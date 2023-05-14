skumria_cost_per_kg = float(input())
caca_cost_per_kg = float(input())
palamud_count = float(input())
safrid_count = float(input())
midi_count = int(input())

palamund_price = skumria_cost_per_kg + (skumria_cost_per_kg * 0.60)
safrid_price = caca_cost_per_kg + ( caca_cost_per_kg * 0.80)
midi_price = midi_count * 7.50

money_needed = palamund_price * palamud_count + safrid_price * safrid_count + midi_price

print(f"{money_needed:.2f}")