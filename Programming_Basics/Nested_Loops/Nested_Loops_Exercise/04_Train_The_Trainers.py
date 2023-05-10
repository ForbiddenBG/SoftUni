judges_count = int(input())
presentation_name = input()

final_grade = 0
presentation_count = 0

while presentation_name != "Finish":
    grade_sum = 0
    for i in range(judges_count):
        grade = float(input())
        grade_sum += grade

    average_grade = grade_sum / judges_count
    print(f"{presentation_name} - {average_grade:.2f}.")

    final_grade += average_grade
    presentation_count += 1

    presentation_name = input()

final_grade = final_grade / presentation_count
print(f"Student's final assessment is {final_grade:.2f}.")
