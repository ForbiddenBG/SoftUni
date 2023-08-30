def grocery_store(**kwargs):
    result = ""
    for k, v in sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0])):
        result += f"{k}: {v}" + "\n"
    return result
