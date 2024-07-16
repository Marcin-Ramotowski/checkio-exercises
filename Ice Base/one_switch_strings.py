#!/usr/bin/env checkio --domain=py run one-switch-strings

# CheckiO platform has a similar missionVerify Anagrams,    but in it you have to determine whether words are anagrams. In this mission, the task will be a little different. You are given two    strings and need to determine whether you can swap two letters in the first string to get the second string. If so (or words are the same) -    returnTrue, if not -False.
# 
# For example, the string"btry", if we swapyandt, we get"byrt".
# 
# Input:Two strings(str).
# 
# Output:Logic value(bool).
# 
# Preconditions:
# 
# All letters are in lower case;Only letters.
# END_DESC

def switch_strings(line: str, result: str) -> bool:
    if line == result:
        return True
    if set(line) != set(result):
        return False
    pairs = zip(line, result)
    diffs = map(lambda x: x[0] != x[1], pairs)
    number_diffs = sum(diffs)
    return number_diffs == 2


print("Example:")
print(switch_strings("btry", "byrt"))

assert switch_strings("btry", "byrt") == True
assert switch_strings("boss", "boss") == True
assert switch_strings("solid", "disel") == False
assert switch_strings("false", "flaes") == False
assert switch_strings("true", "treu") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")