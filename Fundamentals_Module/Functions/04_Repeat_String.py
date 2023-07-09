def repeat_string(string, times):
    return string * times


text = input()
n = int(input())
result = repeat_string(text, n)
print(result)
# print(repeat_string(text, n))

# text = input()
# n = int(input())
#
# x = lambda s, n: s * n
# result = x(text, n)
# print(result)
