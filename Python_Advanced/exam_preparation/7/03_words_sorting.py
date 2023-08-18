def words_sorting(*args):
    words = {}
    value = 0
    for word in args:
        value += sum([ord(x) for x in word])
        words[word] = value
        value = 0
    result = ""
    if sum(words.values()) % 2 == 1:
        sorted_odd_dict = sorted(words.items(), key=lambda kvpt: -kvpt[1])
        for k, v in sorted_odd_dict:
            result += f"{k} - {v}" + "\n"
    else:
        sorted_even_dict = sorted(words.items(), key=lambda kvpt: kvpt[0])
        for k, v in sorted_even_dict:
            result += f"{k} - {v}" + "\n"
    return result.strip()


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))


print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))