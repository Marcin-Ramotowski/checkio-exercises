#!/usr/bin/env checkio --domain=py run count-consecutive-summers

# Positive integers can be expressed as sums of consecutive positive integers in various ways. For example, 42 can be expressed as such a sum in four different ways:(a) 3+4+5+6+7+8+9, (b) 9+10+11+12, (c) 13+14+15 and (d) 42. As the last solution (d) shows, any positive integer can always be trivially expressed as a singleton sum   that consists of that integer alone.
# 
# Compute how many different ways it can be expressed as a sum of consecutive positive integers.
# 
# Input:Int.
# 
# Output:Int.
# 
# Precondition:Input is always a positive integer.
# 
# The mission was taken from Python CCPS 109 Fall 2018. It’s being taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

def count_consecutive_summers(num):
    x = 1
    end = int(num ** (1/2) * 1.5)
    for i in range(2, end+1):
        if i % 2:  # if odd
            if num % i == 0 and num / i > (i-1) / 2:
                x += 1
        else:
            if num % i == i/2 and num / i > i / 2:
                x += 1
    return x


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")