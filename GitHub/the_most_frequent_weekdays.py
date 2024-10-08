#!/usr/bin/env checkio --domain=py run the-most-frequent-weekdays

# What’s your favourite day of the week? Check if it's the most common day of the week in a year.
# 
# You are given a year as an integer (e. g. 2001). You should return the most frequent day(s) of the week in that particular year.    The result has to be a list of days sorted by the order of days in a week (e. g. ['Monday', 'Tuesday']). Week starts with Monday.
# 
# Input:Year as anint.
# 
# Output:The list of most common days sorted by the order of days in a week (from Monday to Sunday).
# 
# Preconditions:Year is between 1 and 9999. Week starts with Monday.
# 
# 
# END_DESC

from datetime import date

def most_frequent_days(year):
    first = date(year,1,1).weekday()
    last = date(year, 12, 31).weekday()
    weekdays = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    score = [weekdays[first]] if first == last else sorted([first, last])
    return score if len(score) == 1 else [weekdays[score[0]], weekdays[score[1]]]


if __name__ == '__main__':
    print("Example:")
    print(most_frequent_days(1084))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert most_frequent_days(1084) == ['Tuesday', 'Wednesday']
    assert most_frequent_days(1167) == ['Sunday']
    assert most_frequent_days(1216) == ['Friday', 'Saturday']
    assert most_frequent_days(1492) == ['Friday', 'Saturday']
    assert most_frequent_days(1770) == ['Monday']
    assert most_frequent_days(1785) == ['Saturday']
    assert most_frequent_days(212) == ['Wednesday', 'Thursday']
    assert most_frequent_days(1) == ['Monday']
    assert most_frequent_days(2135) == ['Saturday']
    assert most_frequent_days(3043) == ['Sunday']
    assert most_frequent_days(2001) == ['Monday']
    assert most_frequent_days(3150) == ['Sunday']
    assert most_frequent_days(3230) == ['Tuesday']
    assert most_frequent_days(328) == ['Monday', 'Sunday']
    assert most_frequent_days(2016) == ['Friday', 'Saturday']
    print("Coding complete? Click 'Check' to earn cool rewards!")