key = int(input())
number_of_lines = int(input())

raw = 0
decrypted = ""

for line in range(1, number_of_lines + 1):
    letters = input()
    raw = ord(letters) + key
    decrypted += chr(raw)

print(decrypted)
