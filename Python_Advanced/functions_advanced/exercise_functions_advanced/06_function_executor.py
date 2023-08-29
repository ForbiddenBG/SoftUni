def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    result = []
    for func_ref, func_params in args:
        func_result = func_ref(*func_params)
        result.append(func_result)
    return result


# def sum_numbers(num1, num2):
#     return num1 + num2
#
#
# def multiply_numbers(num1, num2):
#     return num1 * num2
#
#
# def make_upper(*strings):
#     result = tuple(s.upper() for s in strings)
#     return result
#
#
# def make_lower(*strings):
#     result = tuple(s.lower() for s in strings)
#     return result
#
#
# def func_executor(*args):
#     executed = []
#     for func_ref, arguments in args:
#         result = func_ref(*arguments)
#         executed.append(f"{func_ref.__name__} - {result}")
#     return '\n'.join(executed)
#
#
# print(func_executor(
#     (sum_numbers, (1, 2)),
#     (multiply_numbers, (2, 4))
# ))
#
# print(func_executor(
#     (make_upper, ("Python", "softUni")),
#     (make_lower, ("PyThOn",)),
# ))
