#!/usr/bin/env checkio --domain=py run greedy-number

# Your mission here is to find the biggest possible number using specific rules.
# 
# The number has a specific length, passed through the second argument.The number consists of digests passed through the first argument.Every digit can be used only once.The order of the digits remains the same.It is always enough digits for the resulting number.Input:Two arguments. String and Integer
# 
# Output:String.
# 
# 
# END_DESC

def greedy_number(line: str, n: int) -> str:
    if n == len(line):
        return line
    maxI = len(line)
    minI = 0
    score = ''
    digits = [x for x in enumerate(line) if minI < x[0] < maxI-n+1]
    while n:
        minI, maxD = max(digits, key=lambda x:x[1])
        score += maxD
        n -= 1
        digits = [x for x in enumerate(line) if minI < x[0] < maxI-n+1]
    return score

print('Example:')
print(greedy_number("571", 2))

assert greedy_number('571', 2) == '71'
assert greedy_number('12', 1) == '2'
assert greedy_number('763832', 3) == '832'
assert greedy_number('4368534743453', 5) == '87453'
assert greedy_number('111121', 3) == '121'
assert greedy_number('54', 2) == '54'


print("The first mission is done! Click 'Check' to earn cool rewards!")