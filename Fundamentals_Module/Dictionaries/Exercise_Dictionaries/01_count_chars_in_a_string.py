word = input().split()

my_dict = {}

for i in range(len(word)):
    for letter in word[i]:
        if letter not in my_dict:
            my_dict[letter] = 1
        else:
            my_dict[letter] += 1

for key, value in my_dict.items():
    print(f"{key} -> {value}")
