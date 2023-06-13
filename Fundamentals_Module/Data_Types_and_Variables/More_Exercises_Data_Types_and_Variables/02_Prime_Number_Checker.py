from math import sqrt

n = int(input())
prime_flag = 0

if n > 1:
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            prime_flag = 1
            break
    if prime_flag == 0:
        print(True)
    else:
        print(False)
else:
    print(False)

# number = int(input())
# counter = 0
# for i in range(1, number + 1):
#     if number % i == 0:
#         counter += 1
#     if counter == 2:
#         print("True")
#     else:
#         print("False")

# number = int(input())
# if number > 1:
#     for i in range(2, number):
#         if number % i == 0:
#             print("False")
#             break
#     else:
#         print("True")
# else:
#     print("False")
