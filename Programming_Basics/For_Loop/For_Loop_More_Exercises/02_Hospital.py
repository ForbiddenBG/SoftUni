period = int(input())

doctors_count = 7
treated_patients = 0
not_treated_patients = 0

for day in range(1, period + 1):
    if day % 3 == 0:
        if not_treated_patients > treated_patients:
            doctors_count += 1
    patients_for_current_day = int(input())
    if doctors_count >= patients_for_current_day:
        treated_patients += patients_for_current_day
    else:
        treated_patients += doctors_count
        not_treated_patients += (patients_for_current_day - doctors_count)

if period:
    print(f"Treated patients: {treated_patients}.")
    print(f"Untreated patients: {not_treated_patients}.")


