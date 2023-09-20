def tags(tag):
    def decorator(func_ref):
        def wrapper(*nums):
            result = func_ref(*nums)
            return f"<{tag}>{result}</{tag}>"
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))