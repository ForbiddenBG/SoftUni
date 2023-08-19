def naughty_or_nice_list(list, *args, **kwargs):
    my_dict = {"Nice": [], "Naughty": [], "Not found": []}

    for x in args:
        intiger, mood = x.split("-")
        value = int(intiger)
        my_list = []
        for value_list, name in list:
            if value == value_list:
                my_list.append(name)
        if len(my_list) != 1:
            continue
        else:
            my_dict[mood].append(my_list[0])
        for index, x in enumerate(list):
            if value == x[0]:
                list.pop(index)
                break

    if kwargs:
        for name_dict, mood_dict in kwargs.items():
            my_second_list = []
            for value_list, name in list:
                if name == name_dict:
                    my_second_list.append(name_dict)
            if len(my_second_list) != 1:
                continue
            else:
                my_dict[mood_dict].append(my_second_list[0])
            for index, x in enumerate(list):
                if name_dict == x[1]:
                    list.pop(index)
                    break
    if list:
        for v, n in list:
            my_dict["Not found"].append(n)

    result = ""
    for k, v in my_dict.items():
        if v:
            result += f"{k}: {', '.join([x for x in v])}" + "\n"

    return result.strip()
