def make_underline(func_ref):
    def wrapper(*args):
        func_result = func_ref(*args)
        return f"<u>{func_result}</u>"

    return wrapper


def make_italic(func_ref):
    def wrapper(*args):
        func_result = func_ref(*args)
        return f"<i>{func_result}</i>"

    return wrapper


def make_bold(func_ref):
    def wrapper(*args):
        func_result = func_ref(*args)
        return f"<b>{func_result}</b>"

    return wrapper


# def get_tag(string, tag):
#     return f"<{tag}>{string}</{tag}>"
#
#
# def make_bold(func_ref):
#     def wrapper(*args):
#         result = get_tag(func_ref(*args), "b")
#         return result
#     return wrapper
#
#
# def make_italic(func_ref):
#     def wrapper(*args):
#         result = get_tag(func_ref(*args), "i")
#         return result
#     return wrapper
#
#
# def make_underline(func_ref):
#     def wrapper(*args):
#         result = get_tag(func_ref(*args), "u")
#         return result
#     return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
