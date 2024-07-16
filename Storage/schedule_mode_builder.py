#!/usr/bin/env checkio --domain=py run schedule-mode-builder

# You are given an unordered  list of tasks. Each task is as string, which incudes a start and end of task and has a view"hh:mm-hh:mm". Tasks are unique. You function must return chronologically sorted, filtered list of tasks, which can be scheduled without overlapping. For this purpose, you are also given amodeas an integer, which tells you the rule of choosing non-overlapping tasks.
# 
# Modes:1: earliest start among available, (if a few variants) shortest duration;2: earliest start among available, (if a few variants) longest duration;3: longesttotalduration of chosen tasks, (if a few variants) larger number of tasks done, (if a few variants) earliest;4: larger number of tasks done, (if a few variants) longesttotalduration of chosen tasks, (if a few variants) earliest.
# 
# At animation tasks are always sorted as earliest start + shortest duration. Each task is positioned on the first "row", where it is not overlapping with the previous task in a "row". If the current task is overlapping with all existed "rows" - the new "row" is started.    For example, for the input[['09:00-10:00', '09:50-10:10', '10:00-11:00', '09:00-09:20', '10:50-11:10'], 2], the animation (solved) would be the following:
# 
# 
# 
# Input:A list of tasks as strings(str).
# 
# Output:A sorted filtered list of tasks as strings(str).
# 
# Examples:
# 
# assert schedule(
#     ["09:00-10:00", "09:50-10:10", "10:00-11:00", "09:00-09:20", "10:50-11:10"], 1
# ) == ["09:00-09:20", "09:50-10:10", "10:50-11:10"]
# assert schedule(
#     ["09:00-10:00", "09:50-10:10", "10:00-11:00", "09:00-09:20", "10:50-11:10"], 2
# ) == ["09:00-10:00", "10:00-11:00"]
# assert schedule(
#     ["09:00-10:00", "09:50-10:10", "10:00-11:00", "09:00-09:20", "10:50-11:10"], 3
# ) == ["09:00-10:00", "10:00-11:00"]
# assert schedule(
#     ["09:00-10:00", "09:50-10:10", "10:00-11:00", "09:00-09:20", "10:50-11:10"], 4
# ) == ["09:00-09:20", "09:50-10:10", "10:50-11:10"]
# 
# END_DESC

def schedule(tasks: list[str], mode: int) -> list[str]:
    # your code here
    return []


print("Example:")
print(
    schedule(
        ["09:00-10:00", "09:50-10:10", "10:00-11:00", "09:00-09:20", "10:50-11:10"], 1
    )
)

# These "asserts" are used for self-checking
assert schedule(
    ["09:00-10:00", "09:50-10:10", "10:00-11:00", "09:00-09:20", "10:50-11:10"], 1
) == ["09:00-09:20", "09:50-10:10", "10:50-11:10"]
assert schedule(
    ["09:00-10:00", "09:50-10:10", "10:00-11:00", "09:00-09:20", "10:50-11:10"], 2
) == ["09:00-10:00", "10:00-11:00"]
assert schedule(
    ["09:00-10:00", "09:50-10:10", "10:00-11:00", "09:00-09:20", "10:50-11:10"], 3
) == ["09:00-10:00", "10:00-11:00"]
assert schedule(
    ["09:00-10:00", "09:50-10:10", "10:00-11:00", "09:00-09:20", "10:50-11:10"], 4
) == ["09:00-09:20", "09:50-10:10", "10:50-11:10"]
assert schedule(
    ["09:00-10:00", "10:00-10:10", "09:10-09:20", "09:30-09:40", "09:50-10:00"], 1
) == ["09:00-10:00", "10:00-10:10"]
assert schedule(
    ["09:00-10:00", "10:00-10:10", "09:10-09:20", "09:30-09:40", "09:50-10:00"], 2
) == ["09:00-10:00", "10:00-10:10"]
assert schedule(
    ["09:00-10:00", "10:00-10:10", "09:10-09:20", "09:30-09:40", "09:50-10:00"], 3
) == ["09:00-10:00", "10:00-10:10"]
assert schedule(
    ["09:00-10:00", "10:00-10:10", "09:10-09:20", "09:30-09:40", "09:50-10:00"], 4
) == ["09:10-09:20", "09:30-09:40", "09:50-10:00", "10:00-10:10"]

print("The mission is done! Click 'Check Solution' to earn rewards!")