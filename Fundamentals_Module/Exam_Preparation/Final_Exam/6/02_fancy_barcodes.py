import re

number = int(input())
digits = ""

for _ in range(number):
    text = input()
    pattern = r"(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)"
    valid_products = re.match(pattern, text)
    digits = ""
    if valid_products:
        for el in valid_products.group():
            if el.isdigit():
                digits += el
        if digits == "":
            print("Product group: 00")
        else:
            print(f"Product group: {digits}")
    else:
        print("Invalid barcode")
