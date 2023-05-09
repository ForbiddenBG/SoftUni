movie_name = input()
student_count = 0
standard_count = 0
kid_count = 0

while not movie_name == "Finish":
    free_seats = int(input())
    taken_seats = 0
    for i in range(0, free_seats):
        current_ticket = input()
        if current_ticket == "student":
            student_count += 1
        elif current_ticket == "standard":
            standard_count += 1
        elif current_ticket == "kid":
            kid_count += 1
        elif current_ticket == "End":
            break
        taken_seats += 1
    percent = taken_seats / free_seats * 100
    print(f"{movie_name} - {percent:.2f}% full.")
    movie_name = input()

total_tickets = student_count + standard_count + kid_count
print(f"Total tickets: {total_tickets}")
student_percent = student_count / total_tickets * 100
print(f"{student_percent:.2f}% student tickets.")
standard_percent = standard_count / total_tickets * 100
print(f"{standard_percent:.2f}% standard tickets.")
kid_percent = kid_count / total_tickets * 100
print(f"{kid_percent:.2f}% kids tickets.")