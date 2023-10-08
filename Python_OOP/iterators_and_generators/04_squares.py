def squares(num):
    i = 1
    while i <= num:
        yield i * i
        i += 1
        