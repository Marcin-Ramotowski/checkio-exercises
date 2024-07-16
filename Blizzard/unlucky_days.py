#!/usr/bin/env checkio --domain=py run unlucky-days

# Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year.
# 
# Find the number of Friday 13th in the given year.
# 
# Input:Year as an integer.
# 
# Output:Number of Black Fridays in the year as an integer.
# 
# Precondition:1000 < |year| < 3000
# 
# 
# END_DESC

from datetime import date

def checkio(year: int) -> int:
    x = 0
    for i in range(1,13):
        day = date(year, i, 13)
        weekday = day.weekday()
        if weekday == 4:
            x += 1
    return x

if __name__ == '__main__':
    print("Example:")
    print(checkio(2015))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"
    print("Coding complete? Click 'Check' to earn cool rewards!")