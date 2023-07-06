import re

number = int(input())

for _ in range(number):
    password = input()
    pattern = r"(.+)(\>)(?P<num>\d+{3})(\|)(?P<word>[a-z]+{3})\4(?P<word2>[A-Z]+{3})\4(?P<word3>[a-z!*@#]+{3})?(\<)\1"
    valid_passowrd = [el.groupdict() for el in re.finditer(pattern, password)]
    if valid_passowrd:
        for el in valid_passowrd:
            new_pass = ""
            new_pass += el['num']
            new_pass += el['word']
            new_pass += el['word2']
            new_pass += el['word3']
            print(f"Password: {new_pass}")
        new_pass = ""
    else:
        print("Try another password!")
