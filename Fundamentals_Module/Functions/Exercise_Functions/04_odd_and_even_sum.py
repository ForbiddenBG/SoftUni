def get_odd_even_sum(nums_as_string):
    odd_sum = 0
    even_sum = 0
    for char in nums_as_string:
        current_char_as_num = int(char)
        if current_char_as_num % 2 == 0:
            even_sum += current_char_as_num
        else:
            odd_sum += current_char_as_num
    return [odd_sum, even_sum]


number_as_string = input()
result = get_odd_even_sum(number_as_string)
even_sum = result[1]
odd_sum = result[0]
print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
