exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes

difference = arrival_time - exam_time
text = ""
if difference < -30:
    text = "Early"
elif difference <= 0:
    text = "On time"
else:
    text = "Late"

print(text)

if difference != 0:
    hours = abs(difference) // 60
    minutes = abs(difference) % 60

    if hours > 0:
        if difference < 0:
            print(f"{hours}:{minutes:02d} hours before the start")
        else:
            print(f"{hours}:{minutes:02d} hours after the start")
    else:
        if difference < 0:
            print(f"{minutes} minutes before the start")
        else:
            print(f"{minutes} minutes after the start")