#!/usr/bin/env checkio --domain=py run number-factory

# You are given a two or more digits numberN.    For this mission, you should find the smallest positive number ofX,    such that the product of its digits is equal to N.    If X does not exist, then return 0.
# 
# Let's examine the example. N = 20. We can factorize this number as 2*10, but 10 is not a digit.    Also we can factorize it as 4*5 or 2*2*5. The smallest number for 2*2*5 is 225, for 4*5 -- 45. So we select 45.
# 
# Hints:Remember prime numbers (numbers divisible by only one) and be careful with endless loops.
# 
# Input:A number N as an integer.
# 
# Output:The number X as an integer.
# 
# How it is used:This task will teach you how to work with numbers in code.    You can factorize numbers and reconstruct them into new numbers.    Of course you can solve this problem with brute force,    but is that the best way?    Numbers are the foundation of mathematics and programming.
# 
# Precondition:
# 9 < N < 105.
# 
# 
# END_DESC

def checkio(n: int):
    factors = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            if k > 10:
                return 0
            factors.append(k)
        k += 1
    factors2 = ''.join(list(map(str, factors)))
    factors3 = factors2
    instructions = {'222': '8', '22': '4', '23': '6', '33': '9'}
    instructions2 = {'222': '8', '23': '6', '22': '4', '33': '9'}
    for commend in instructions:
        factors2 = factors2.replace(commend, instructions[commend])
    for commend in instructions2:
        factors3 = factors3.replace(commend, instructions[commend])
    factors2 = int(''.join(sorted(factors2)))
    factors3 = int(''.join(sorted(factors3)))
    return min(factors2, factors3)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")