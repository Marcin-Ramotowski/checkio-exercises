#!/usr/bin/env checkio --domain=py run house-password

# Stephan and Sophia forget about security and use simple passwords for everything.    Help Nikola develop a password security check module.    The password will be considered strong enough if its length is greater than or equal to 10 symbols,    it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it.    The password contains only ASCII latin letters or digits.
# 
# Input:A password as a string.
# 
# Output:Is the password safe or not as a boolean or any data type that can be    converted and processed as a boolean. In the results you will see the converted results.
# 
# 
# Precondition:
# re.match("[a-zA-Z0-9]+", password)
# 0 < len(password) ≤ 64
# 
# 
# END_DESC

import re

def checkio(password: str) -> bool:
    if len(password) < 10:
        return False
    tests = ['[0-9]','[A-Z]','[a-z]']
    for test in tests:
        if not(re.search(test, password)):
            return False
    return True