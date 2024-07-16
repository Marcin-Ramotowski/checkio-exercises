#!/usr/bin/env checkio --domain=py run work-schedule-generator

# 
# 
# You are given a sequence of employees with their work preferences and skills. Also you have business needs as required working time and tasks. Your function should return a schedule, that satisfies business needs with available employees (if it's possible). Now, let's dive into the details.
# 
# staffis a dictionary, where keys are names of employees and values are  dictionaries as well. Every values dictionary includes three key-value pairs:"pref_shifts"- list of strings: shifts, employee wants to work at (may be"first","second"or both in this order);"days_off"- list of strings: days, employee wants to be off (full names of weekdays);"skills"- list of strings: jobs, employee may do.
# 
# business_needsis a list of three values: a weekday, for which to make schedule - string; number of shifts to be on this day - integer; tasks, which should be done on this day - list of strings.
# 
# Notice about shifts. Each employee may work at first shift, second or both (all day), excluding his/her days off. Number of shifts for business means number of different shifts to be present at this day. For example, if number of shifts3, in may be covered by an employee, who works full day (both his shifts, "first" and "second", total - 2) and any employee more (because every employee has at least one shift), or by three shifts from different employee. Number of shifts should be divided equally between"first"and"second"day shifts. If number of shifts is odd (and not equal 1),"first"day shift must include one shift more, than"second"day shift.
# 
# Skills may be partly/totally the same for different employees. So, when you fill the day shifts, chose employees with less number of skills - they are usually less paid. If the number is the same - chose by name alphabetically. From the point of employees engagement, first day shift has priority: it's more important to have employees with less number of skills there. Tasks is a minimum sequence to be done - the sequence of aggregated skills for this day may be wider. Each task must be done (covered with respective skill) by someone at"first"or"second"dayshift.
# 
# Your function should return a list of two lists (day shifts) with alphabetically sorted names of employees, which are going to work at respective day shift. If the number of shifts is1- one of inner lists will be empty. If it's not possible to make schedule - both inner lists should be empty.
# 
# Input:Two arguments: a dictionary with employees data, a list with business need description.
# 
# Output:A list of two lists with names as strings.
# 
# Examples:
# 
# assert schedule_generator(
#     {
#         "Charlie": {
#             "pref_shifts": ["first", "second"],
#             "days_off": ["Wednesday"],
#             "skills": ["customer service", "inventory", "cleaning", "sales"],
#         },
#         "Alice": {
#             "pref_shifts": ["second"],
#             "days_off": ["Saturday", "Sunday"],
#             "skills": ["customer service", "sales"],
#         },
#         "Bob": {
#             "pref_shifts": ["first"],
#             "days_off": ["Monday", "Tuesday"],
#             "skills": ["customer service", "inventory"],
#         },
#     },
#     ["Monday", 1, ["customer service", "sales"]],
# ) == [[], ["Alice"]]
# assert schedule_generator(
#     {
#         "Charlie": {
#             "pref_shifts": ["first", "second"],
#             "days_off": ["Wednesday"],
#             "skills": ["customer service", "inventory", "cleaning", "sales"],
#         },
#         "Alice": {
#             "pref_shifts": ["second"],
#             "days_off": ["Saturday", "Sunday"],
#             "skills": ["customer service", "sales"],
#         },
#         "Bob": {
#             "pref_shifts": ["first"],
#             "days_off": ["Monday", "Tuesday"],
#             "skills": ["customer service", "inventory"],
#         },
#     },
#     ["Monday", 2, ["customer service", "sales"]],
# ) == [["Charlie"], ["Alice"]]
# assert schedule_generator(
#     {
#         "Charlie": {
#             "pref_shifts": ["first", "second"],
#             "days_off": ["Wednesday"],
#             "skills": ["customer service", "inventory", "cleaning", "sales"],
#         },
#         "Alice": {
#             "pref_shifts": ["second"],
#             "days_off": ["Saturday", "Sunday"],
#             "skills": ["customer service", "sales"],
#         },
#         "Bob": {
#             "pref_shifts": ["first"],
#             "days_off": ["Monday", "Tuesday"],
#             "skills": ["customer service", "inventory"],
#         },
#     },
#     ["Wednesday", 1, ["customer service", "sales", "inventory"]],
# ) == [[], []]
# 
# END_DESC

def schedule_generator(staff: dict, business_needs: list) -> list[list[str]]:
    # your code here
    return [[], []]


print("Example:")
print(
    schedule_generator(
        {
            "Charlie": {
                "pref_shifts": ["first", "second"],
                "days_off": ["Wednesday"],
                "skills": ["customer service", "inventory", "cleaning", "sales"],
            },
            "Alice": {
                "pref_shifts": ["second"],
                "days_off": ["Saturday", "Sunday"],
                "skills": ["customer service", "sales"],
            },
            "Bob": {
                "pref_shifts": ["first"],
                "days_off": ["Monday", "Tuesday"],
                "skills": ["customer service", "inventory"],
            },
        },
        ["Monday", 1, ["customer service", "sales"]],
    )
)

# These "asserts" are used for self-checking
assert schedule_generator(
    {
        "Charlie": {
            "pref_shifts": ["first", "second"],
            "days_off": ["Wednesday"],
            "skills": ["customer service", "inventory", "cleaning", "sales"],
        },
        "Alice": {
            "pref_shifts": ["second"],
            "days_off": ["Saturday", "Sunday"],
            "skills": ["customer service", "sales"],
        },
        "Bob": {
            "pref_shifts": ["first"],
            "days_off": ["Monday", "Tuesday"],
            "skills": ["customer service", "inventory"],
        },
    },
    ["Monday", 1, ["customer service", "sales"]],
) == [[], ["Alice"]]
assert schedule_generator(
    {
        "Charlie": {
            "pref_shifts": ["first", "second"],
            "days_off": ["Wednesday"],
            "skills": ["customer service", "inventory", "cleaning", "sales"],
        },
        "Alice": {
            "pref_shifts": ["second"],
            "days_off": ["Saturday", "Sunday"],
            "skills": ["customer service", "sales"],
        },
        "Bob": {
            "pref_shifts": ["first"],
            "days_off": ["Monday", "Tuesday"],
            "skills": ["customer service", "inventory"],
        },
    },
    ["Monday", 2, ["customer service", "sales"]],
) == [["Charlie"], ["Alice"]]
assert schedule_generator(
    {
        "Charlie": {
            "pref_shifts": ["first", "second"],
            "days_off": ["Wednesday"],
            "skills": ["customer service", "inventory", "cleaning", "sales"],
        },
        "Alice": {
            "pref_shifts": ["second"],
            "days_off": ["Saturday", "Sunday"],
            "skills": ["customer service", "sales"],
        },
        "Bob": {
            "pref_shifts": ["first"],
            "days_off": ["Monday", "Tuesday"],
            "skills": ["customer service", "inventory"],
        },
    },
    ["Wednesday", 1, ["customer service", "sales", "inventory"]],
) == [[], []]

print("The mission is done! Click 'Check Solution' to earn rewards!")