last_sector = input()
rows_count_sector_one = int(input())
seats_count_odd_row = int(input())

last_sector = ord(last_sector)


for sector in range(1, last_sector + 1):
    for row in range(1, rows_count_sector_one + 1):
        rows_count_sector_one += 1
        for seat_odd in range(1, seats_count_odd_row + 1):
            total_seats = seat_odd
            total_seats = ord(total_seats)
            for seat_even in range(0, seats_count_odd_row + 2, 2):
                total_seats = seat_even
                total_seats = ord(total_seats)

total_seats = ord(total_seats)
seat_even = ord(seat_even)

print(f"{sector}{row}{total_seats}")