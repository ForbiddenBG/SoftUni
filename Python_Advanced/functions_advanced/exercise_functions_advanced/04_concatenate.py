def concatenate(*args, **kwargs):
    result = ""
    for el in args:
        result += el
        for k, v in kwargs.items():
            if k in result:
                result = result.replace(k, kwargs[k])
    return result


# def concatenate(*args):
#     result = ""
#     for word in args:
#         result += word
#     return result
