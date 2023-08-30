def palindrome(text, idx):
    if idx == len(text) // 2:
        return f"{text} is a palindrome"

    left = text[idx]
    right = text[len(text) - 1 - idx]

    if left != right:
        return f"{text} is not a palindrome"

    return palindrome(text, idx + 1)

# def palindrome(word, idx):
#     if idx == len(word) // 2:
#         return f"{word} is a palindrome"
#
#     if word[idx] != word[len(word) - idx - 1]:
#         return f"{word} is not a palindrome"
#
#     return palindrome(word, idx + 1)
