spell = input()

command = input()
while not command == "Abracadabra":
    main_data = command.split()
    if main_data[0] == "Abjuration":
        spell = spell.upper()
        print(spell)
    elif main_data[0] == "Necromancy":
        spell = spell.lower()
        print(spell)
    elif main_data[0] == "Illusion":
        index, letter = main_data[1:]
        index = int(index)
        if index in range(len(spell)):
            spell = spell[0:index] + letter + spell[index + 1:]
            print("Done")
        else:
            print("The spell was too weak.")
    elif main_data[0] == "Divination":
        first_substring, second_substring = main_data[1:]
        if first_substring in spell:
            spell = spell.replace(first_substring, second_substring)
            print(spell)
        else:
            pass
    elif main_data[0] == "Alteration":
        substring = main_data[1]
        if substring in spell:
            spell = spell.replace(substring, "")
            print(spell)
        else:
            pass
    else:
        print("The spell did not work!")

    command = input()
