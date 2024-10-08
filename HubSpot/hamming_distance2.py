#!/usr/bin/env checkio --domain=py run hamming-distance2

# The Hamming distance between two binary integers is the number of bit positions that differs    (read more about the Hamming distance on Wikipedia).    For example:
# 
# 
#     117 = 0 1 1 1 0 1 0 1
#      17 = 0 0 0 1 0 0 0 1
#       H = 0+1+1+0+0+1+0+0 = 3
# 
# You are given two positive numbers (N, M) in decimal form.    You should calculate the Hamming distance between these two numbers in binary form.
# 
# Input:Two arguments as integers.
# 
# Output:The Hamming distance as an integer.
# 
# Precondition:
# 0 < n < 106
# 0 < m < 106
# 
# 
# 
# END_DESC

def checkio(a, b):
    a,b = bin(a)[2:], bin(b)[2:]
    l1, l2 = len(a), len(b)
    l = l1
    if l1 > l2:
        diff = l1 - l2
        b = '0' * diff + b
    elif l2 > l1:
        diff = l2 - l1
        a = '0' * diff + a
        l = l2
    counter = 0
    for i in range(l):
        x, y = a[i], b[i]
        if x != y:
            counter += 1
    return counter

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"