#!/usr/bin/env checkio --domain=py run stressful-subject

# The function should recognize if a subject line is stressful.    A stressful subject line means that all letters are in uppercase, and/or the whole line ends    by at least 3 exclamation marks, and/or contains at least one of the following    “red” words: "help", "asap", "urgent". Any of those "red" words can be spelled    in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a    very loooong way "HHHEEEEEEEEELLP," they just can't have any other letters interspersed between them.
# 
# Input:Subject line as a string.
# 
# Output:Boolean.
# 
# Precondition:Subject can be up to 100 letters
# 
# 
# END_DESC

import re


def is_stressful(line: str) -> bool:
    """
    recognize stressful subject
    """
    if line.isupper() or line.endswith('!!!'):
        return True
    PATTERNS = ['h+[!-.]*e+[!-.]*l+[!-.]*p+[!-.]*',
                'a+[!-.]*s+[!-.]*a+[!-.]*p+[!-.]*',
                'u+[!-.]*r+[!-.]*g+[!-.]*e+[!-.]*n+[!-.]*t+[!-.]*']
    flag = re.IGNORECASE
    for pattern in PATTERNS:
        if re.search(pattern, line, flags=flag):
            return True
    return False


print("Example:")
print(is_stressful("Hi"))

assert is_stressful("Hi") == False
assert is_stressful("I neeed HELP") == True
assert is_stressful("I neeed HLEP") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")