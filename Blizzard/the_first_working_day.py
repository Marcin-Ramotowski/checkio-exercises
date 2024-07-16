#!/usr/bin/env checkio --domain=py run the-first-working-day

# As the input you’ll get the date of the first vacation day in the format 'YYYY-MM-DD' and the total number of vacation days. Your task is to find out which day will be the first working day after the vacation. If it’ll be Saturday or Sunday then it should be the next Monday.
# In this mission you have to ignore national holidays and consider only Saturdays and Sundays.
# Also don't forget about February 29th in the leap year and the situation when the vacation starts at the end of December of the one year and ends at the beginning of the next year.
# 
# Input:The first day of the vacation and the number of days in it.
# 
# Output:The date of the first working day.
# 
# Precondition:
# 1900 <= year <= 2100
# 
# 
# END_DESC

from datetime import date, timedelta

def vacation(date1, days):
    a = date1.split("-")
    data = date(int(a[0]), int(a[1]), int(a[2]))
    days = timedelta(days)
    data += days
    w = data.weekday()
    if w == 5 or w == 6:
        number = 7 - w
        days = timedelta(number)
        data += days
    data = str(data)
    return data

if __name__ == '__main__':
    print("Example:")
    print(vacation('2018-07-01', 14))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert vacation('2018-07-01', 14) == '2018-07-16'
    assert vacation('2018-02-19', 10) == '2018-03-01'
    assert vacation('2000-02-28', 5) == '2000-03-06'
    assert vacation('1999-12-20', 14) == '2000-01-03'
    print("Coding complete? Click 'Check' to earn cool rewards!")