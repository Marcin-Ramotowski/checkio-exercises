#!/usr/bin/env checkio --domain=py run ryerson-letter-grade

# Given the grade percentage for the course, calculate and return the letter grade that would appear in the Ryerson’s grade transcript, as defined on the pageRyerson Grade Scales. The letter grade should be returned as a string that consists of the uppercase letter followed by the possible modifier  "+"  or  "-" .
# 
# Input:Int. Grade percentage.
# 
# Output:Str.  The letter grade.
# 
# Precondition:argument can be from 0 to 150
# 
# The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

TABLE = '''
A 85-89%
A- 80-84%
B+ 77-79%
B 73-76%
B- 70-72%
C+ 67-69%
C 63-66%
C- 60-62%
D+ 57-59%
D 53-56%
D- 50-52%
'''

INTERVALS= TABLE.splitlines()[1:]
GRADESCALE = dict([(reversed(inter.split())) for inter in INTERVALS])

def ryerson_letter_grade(pct: int) -> str:
    if  49 < pct < 90:
        for key in GRADESCALE:
            start = int(key[:2])
            end = int(key[3:5])
            if  start <= pct <= end:
                return GRADESCALE[key] 
    else:
        return 'F' if pct < 50 else 'A+'