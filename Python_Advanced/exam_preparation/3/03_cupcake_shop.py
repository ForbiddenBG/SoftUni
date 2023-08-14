def stock_availability(boxes, *args):
    if args[0] == "delivery":
        for el in range(len(args)):
            if args[el] != "delivery":
                boxes.append(args[el])
    elif args[0] == "sell":
        if len(args) > 1:
            num = str(args[1])
            if num.isdigit():
                number = int(num)
                boxes = boxes[number::]
            else:
                for el in args[1:]:
                    while el in boxes:
                        boxes.remove(el)
        else:
            boxes.remove(boxes[0])
    return boxes


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
