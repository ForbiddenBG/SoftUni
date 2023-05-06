first_contestant = int(input())
second_contestant = int(input())
third_contestant = int(input())

total_time = first_contestant + second_contestant + third_contestant

minutes = total_time // 60
seconds = total_time % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")