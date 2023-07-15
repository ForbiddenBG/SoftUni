all_palindromes = [word for word in input().split() if word == word[::-1]]
searched_palindrome = input()
print(all_palindromes)
print(f"Found palindrome {all_palindromes.count(searched_palindrome)} times")

# words = input().split()
# palindrome = input()
#
# print([el for el in words if el == el[::-1]])
# print(f"Found palindrome {[el for el in words if palindrome == el[::-1]].count(palindrome)} times")
