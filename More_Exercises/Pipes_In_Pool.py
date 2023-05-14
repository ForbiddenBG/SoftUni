capacity_pool_liters = int(input())
debit_pipe_one = int(input())
debit_pipe_two = int(input())
hours_missing = float(input())

capacity_full_from_pipe_one = debit_pipe_one * hours_missing
capacity_full_from_pipe_two = debit_pipe_two * hours_missing
pipes_total_water = capacity_full_from_pipe_one + capacity_full_from_pipe_two

capacity_full_for_hours = (pipes_total_water * 100) / capacity_pool_liters

percent_first_pipe = (capacity_full_from_pipe_one * 100) / pipes_total_water
percent_second_pipe = (capacity_full_from_pipe_two * 100) / pipes_total_water

difference = pipes_total_water - capacity_pool_liters

if capacity_pool_liters >= pipes_total_water:
    print(f"The pool is {capacity_full_for_hours:.2f}% full. Pipe 1: {percent_first_pipe:.2f}%. Pipe 2: {percent_second_pipe:.2f}%.")
else:
    print(f"For {hours_missing:.2f} hours the pool overflows with {difference:.2f} liters.")











