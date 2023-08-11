def start_spring(**kwargs):
    my_dict = {}
    for k, v in kwargs.items():
        if v not in my_dict:
            my_dict[v] = []
        my_dict[v].append(k)
    sorted_num_elements = sorted(my_dict.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ""
    for k, v in sorted_num_elements:
        result += f"{k}:" + "\n"
        for x in sorted(v):
            result += f"-{x}" + "\n"
    return result.strip()


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))


example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird", }
print(start_spring(**example_objects))


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
