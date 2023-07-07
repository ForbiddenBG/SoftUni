words = {}

string = input().split(" | ")
for el in string:
    word, definition = el.split(": ")
    if word not in words:
        words[word] = []
    words[word].append(definition)

teacher = input().split(" | ")

sorted_words = sorted(words.items(), key=lambda kvp: len(kvp[1]), reverse=True)
sorted_alpha = sorted(words.items(), key=lambda kvp: kvp[0])

command = input()
# if command == "Test":
#     for w in teacher:
#         my_dict = {}
#         if w in words:
#             for el in words[w]:
#                 my_dict[el] = len(el)
#             my_dict = sorted(my_dict.items(), key=lambda kvp: kvp[1], reverse=True)
#             print(f"{w}:")
#             for i in my_dict:
#                 print(f" -{i[0]}")
if command == "Test":
    for w in teacher:
        if w in words:
            for k, v in sorted_words:
                if k == w:  # така принтваш само ако я има в teacher
                    print(f"{k}:")
                    for vv in sorted(v, key=lambda x: -len(x)):  # тука ги търси в сортираните валюс
                        print(f" -{vv}")
        else:
            pass
elif command == "Hand Over":
    for k, v in sorted(words.items(), key=lambda kvp: kvp[0]):
        print(f"{k}", end=" ")
