string = input().split()

command = input()
while not command == "Stop":
    main_data = command.split()
    if main_data[0] == "Delete":
        index = main_data[1]
        index = int(index)
        if index in range(len(string)):
            string.remove(string[index+1])
    elif main_data[0] == "Swap":
        word1, word2 = main_data[1:]
        if word1 in string and word2 in string:
            index1 = string.index(word1)
            index2 = string.index(word2)
            string.remove(word1)
            string.insert(index1, word2)
            string.remove(word2)
            string.insert(index2, word1)
    elif main_data[0] == "Put":
        word, index = main_data[1:]
        index = int(index)
        if index in range(len(string)):
            string.insert(index-1, word)
    elif main_data[0] == "Sort":
        string = sorted(string, key=lambda x: -x)
    elif main_data[0] == "Replace":
        word1, word2 = main_data[1:]
        if word2 in string:
            index = string.index(word2)
            string.remove(word2)
            string.insert(index, word1)
    command = input()

print(f"{' '.join(string)}")
