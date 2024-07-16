#!/usr/bin/env checkio --domain=py run currency-style

# "Well, it's that time of the month again. Payroll checks for our employees,      which require your signatures. And no forgetting to sign the big ones!"
# -- Trading Places
# 
# Many countries use different conventions for the thousands separator and decimal mark.  For example in the Netherlands    one million one thousand two hundred and eighty one-hundredths is written as 1.001.200,80, but in the US this is written    as 1,001,200.80.  Use your coding skills to convert dollars in the first style (Netherlands, Germany, Turkey,    Brazil, and others) to the second style (US, UK, Canada, China, Japan, Mexico, and others).
# 
# Only currency amounts in dollars should be converted: $1.234,50 to $1,234.50, $1.000 to $1,000, and $4,57 to $4.57.    Don't accidentally convert your router's IP address 192.168.1.1.  You should leave currency noted in the US style unchanged.
# 
# Input:A string containing dollar amounts to be converted.
# 
# Output:A string with converted currencies.
# 
# Precondition:0 < len(text) ≤ 1000;
# len(fractional_part_of_currency) in {0,2};
# all(s[-1].isdigit() for s in currency_substrings);
# all(s[0] == '$' for s in currency_substrings)
# 
# 
# 
# END_DESC

import re

def checkio(data:str) ->str:
    ''' Zmienia format waluty.'''
    if '$' not in data:
        return data.replace(',','.')
    money = data.split('$')
    money = ['$' + el for el in money]
    scores = []
    for m in money:
        searching = re.search('\d',m[::-1]) # ::-1 means that text is reversed
        if searching != None:
            end = searching.start() # because text is reversing while searching
        else:
            scores.append(m[1:])
            continue
        if len(m) < 3:
            scores.append(m)
        elif m[-end-3] == ',':
            part1 = m[:-end-3].replace('.',',')
            part2 = m[-end-3:].replace(',','.')
            score = part1 + part2
            scores.append(score)
        elif m[-end-3].isdigit():
            if m.count('.') > 0:
                scores.append(m.replace('.',','))
            else:
                scores.append(m)
        else:
            scores.append(m)
    return ''.join(scores)