import sys

sum_odd = 0
sum_even = 0
oddmin = sys.maxsize
oddmax = -sys.maxsize
evenmin = sys.maxsize
evenmax = -sys.maxsize

n = int(input())

for i in range(1, n + 1):
    new_number = float(input())
    if i % 2 == 0:
        sum_even += new_number
        if new_number > evenmax:
            evenmax = new_number
        if new_number < evenmin:
            evenmin = new_number
    else:
        sum_odd += new_number
        if new_number > oddmax:
            oddmax = new_number
        if new_number < oddmin:
            oddmin = new_number

print(f"OddSum={sum_odd:.2f},")

if oddmin == sys.maxsize:
    print(f"OddMin=No,")
else:
    print(f"OddMin={oddmin:.2f},")
if oddmax == -sys.maxsize:
    print(f"OddMax=No,")
else:
    print(f"OddMax={oddmax:.2f},")

print(f"EvenSum={sum_even:.2f},")

if evenmin == sys.maxsize:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={evenmin:.2f},")
if evenmax == -sys.maxsize:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={evenmax:.2f}")
