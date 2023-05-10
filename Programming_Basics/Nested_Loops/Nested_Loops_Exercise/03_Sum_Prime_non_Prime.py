command = input()
sum_primes = 0
sum_non_primes = 0

while command != "stop":
    number = int(command)

    denominator_count = 0
    if number < 0:
        print(f"Number is negative.")
        command = input()
        continue

    for i in range(2, number + 1):
        if number % i == 0:
            denominator_count += 1

    if denominator_count == 1:
        sum_primes += number
    else:
        sum_non_primes += number

    command = input()
print(f"Sum of all prime numbers is: {sum_primes}")
print(f"Sum of all non prime numbers is: {sum_non_primes}")
