#!/usr/bin/env checkio --domain=py run working-hours-calculator

# Write a function that takes two dates and two times as input and returns the total number of working hours between the two dates (incl. both). Times representing the start and end of a workday. Working hours are defined as the time between the end and start times, Monday through Friday, excluding holidays. So the function also takes an argument that specifies a list of holidays to exclude (could be empty).
# 
# Time may have minutes. Convert them into float as minutes/60 with two-digits precision.
# 
# Input:Five arguments: two dates as strings(str), two times as strings, holidays aslistof strings.
# 
# Output:Number of total working hours as integer or float(int | float).
# 
# Examples:
# 
# assert working_hours("2023-03-01", "2023-03-01", "09:00", "17:00", []) == 8
# assert working_hours("2023-03-01", "2023-03-02", "09:00", "17:00", []) == 16
# assert working_hours("2023-03-01", "2023-03-03", "09:00", "17:00", ["2023-03-01"]) == 16
# assert (
#     working_hours("2023-03-01", "2023-03-05", "08:45", "17:10", ["2023-03-03"]) == 16.83
# )
# 
# END_DESC

def working_hours(
    date1: str, date2: str, start_time: str, end_time: str, holy: list[str]
) -> int | float:
    # your code here
    return 0


print("Example:")
print(working_hours("2023-03-01", "2023-03-01", "09:00", "17:00", []))

# These "asserts" are used for self-checking
assert working_hours("2023-03-01", "2023-03-01", "09:00", "17:00", []) == 8
assert working_hours("2023-03-01", "2023-03-02", "09:00", "17:00", []) == 16
assert working_hours("2023-03-01", "2023-03-03", "09:00", "17:00", ["2023-03-01"]) == 16
assert (
    working_hours("2023-03-01", "2023-03-05", "08:45", "17:10", ["2023-03-03"]) == 16.83
)

print("The mission is done! Click 'Check Solution' to earn rewards!")