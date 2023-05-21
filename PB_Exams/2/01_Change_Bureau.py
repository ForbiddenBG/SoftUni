bitcoins_count = int(input())
juans_count = float(input())
commision = float(input()) / 100

bit_lv = bitcoins_count * 1168

jua_usd = juans_count * 0.15
jua_lv = jua_usd * 1.76

total_lv = bit_lv + jua_lv
euros = total_lv / 1.95

final = euros - (euros * commision)
final = float(final)

print(f"{final:.2f}")