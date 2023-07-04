import re

new_string = ""
is_done = True

text = input()
while is_done:
    pattern = r"(#|$|%|\*|&)(?P<name>[a-zA-Z]+)\1=(?P<num>\d+)!!(?P<code>[a-zA-Z0-9%\[\]\(\!\)#\'_$&]+)"
    valid_race = [el.groupdict() for el in re.finditer(pattern, text)]
    if valid_race:
        for el in valid_race:
            if int(el['num']) == len(el['code']):
                for char in el['code']:
                    new_string += chr(ord(char) + len(el['code']))
                print(f"Coordinates found! {el['name']} -> {new_string}")
                is_done = False
                break
            else:
                print(f"Nothing found!")
    else:
        print(f"Nothing found!")
    text = input()
