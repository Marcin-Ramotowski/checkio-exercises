#!/usr/bin/env checkio --domain=py run date-and-time-converter

# Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
# Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
# Your task is simple - convert the input date and time from computer format into a "human" format.
# 
# 
# 
# Input:Date and time as a string
# 
# Output:The same date and time, but in a more readable format
# 
# Precondition:
# 0 <  day <= 31
# 0 <  month <= 12
# 1900 <  year <= 3000
# 0 <= hours < 24
# 0 <= minutes < 60
# 
# 
# END_DESC

def date_time(time: str) -> str:
    new = time.split()
    day = int(time[0:2])
    monthnames = ['','January','February','March','April', 'May','June','July','August','September','October','November','Dezember']
    monthnumber = int(time[3:5])
    month = monthnames[monthnumber]
    year = int(new[0][6:])
    hours = int(new[1][0:2])
    if hours != 1:
        hourText = 'hours'
    else:
        hourText = 'hour'
    minutes = int(new[1][3:])
    if minutes != 1:
        minuteText = 'minutes'
    else:
        minuteText = 'minute'
    text = f'{day} {month} {year} year {hours} {hourText} {minutes} {minuteText}'
    return text

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")