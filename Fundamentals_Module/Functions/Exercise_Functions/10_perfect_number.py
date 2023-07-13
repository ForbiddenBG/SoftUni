def is_num_perfect(num):
    proper_divisors = []

    for current_num in range(1, num):
        if num % current_num == 0:
            proper_divisors.append(current_num)

    if sum(proper_divisors) == num:
        return True
    return False


n = int(input())

if is_num_perfect(n):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")


# def perfect_number(n):
#     divisible = []
#     div_count = 0
#
#     for num in range(1, n - 1):
#         if n % num == 0:
#             divisible.append(num)
#         else:
#             continue
#
#     for div in divisible:
#         div_count += div
#
#     if div_count == n:
#         print("We have a perfect number!")
#     else:
#         print("It's not so perfect.")
#
#
# number = int(input())
# perfect_number(number)
