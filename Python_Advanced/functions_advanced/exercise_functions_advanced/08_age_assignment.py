# def age_assignment(*args, **kwargs):
#     result = {}
#     for name in args:
#         first_letter = name[0]
#         age = kwargs[first_letter]
#         result[name] = age
#     return result


def age_assignment(*args, **kwargs):
    result = ""
    for name in sorted(args):
        result += f"{name} is {kwargs[name[0]]} years old." + "\n"
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
