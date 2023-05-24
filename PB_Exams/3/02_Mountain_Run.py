from math import floor
record_sec = float(input())
lenghth = float(input())
time_for_m_per_sec = float(input())

total_sec = lenghth * time_for_m_per_sec

delay = (lenghth / 50) * 30


real_time = floor(total_sec + delay)

if real_time < record_sec:
    print(f"Yes! The new record is {real_time} seconds.")
elif real_time > record_sec:
    print(f"No! He was {abs(record_sec - real_time):.2f} seconds slower.")