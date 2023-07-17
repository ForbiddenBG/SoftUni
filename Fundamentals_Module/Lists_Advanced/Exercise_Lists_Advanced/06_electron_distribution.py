number_of_electrons = int(input())
electrons = []
shell_number = 1

while number_of_electrons > 0:
    max_electrons_in_current_shell = 2 * shell_number ** 2
    if max_electrons_in_current_shell > number_of_electrons:
        electrons.append(number_of_electrons)
    else:
        electrons.append(max_electrons_in_current_shell)
    number_of_electrons -= max_electrons_in_current_shell
    shell_number += 1

print(electrons)

# number_of_electrons = int(input())
#
# my_list = []
# element = 0
#
# while number_of_electrons > 0:
#     element += 1
#     if number_of_electrons < 2*(element**2):
#         my_list.append(number_of_electrons)
#         break
#     my_list.append(2*(element**2))
#     number_of_electrons -= (2*(element**2))
#
# print(my_list)
