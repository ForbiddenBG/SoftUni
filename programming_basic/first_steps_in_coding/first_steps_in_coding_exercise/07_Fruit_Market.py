strawberries_price = float(input())
bananas_count = float(input())
oranges_count = float(input())
raspberries_count = float(input())
strawberries_count = float(input())

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price * 0.6
bananas_price = 0.2 * raspberries_price

total_price = bananas_price * bananas_count + raspberries_count * raspberries_price + strawberries_count * strawberries_price + oranges_price * oranges_count

print(total_price)