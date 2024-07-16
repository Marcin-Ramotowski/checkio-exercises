#!/usr/bin/env checkio --domain=py run ugly-numbers

# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ... shows the first 11 ugly numbers. By convention, 1 is included.Write a program to find and print the N’th ugly number
# 
# 
# 
# Input:N, int.
# 
# Output:N'th Ugly Number, int.
# 
# Precondition:Given int is below or equal of 1500
# 
# The mission was taken from ICPC challenge
# 
# 
# END_DESC

def ugly_number(n):
    uglies = gen_ugly()
    for x in range(n):
        temp = next(uglies)
    return temp

def gen_ugly():
    i = 1
    while True:
        if i < 7:
            yield i
            i += 1
        x = i
        if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
            while x % 2 == 0:
                x //= 2
            while x % 3 == 0:
                x //= 3
            while x % 5 == 0:
                x //= 5
            if x == 1:
                yield i
        i += 1


if __name__ == "__main__":
    print("Example:")
    print(ugly_number(4))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert ugly_number(4) == 4
    assert ugly_number(6) == 6
    assert ugly_number(11) == 15
    print("Ugly Numbers coding complete? Click 'Check' to earn cool rewards!")