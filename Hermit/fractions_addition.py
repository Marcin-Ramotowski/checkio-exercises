#!/usr/bin/env checkio --domain=py run fractions-addition

# Your task is to write a function which takes the tuple of tuples containing fractions as an argument and returns the sum of those fractions. The fractions will look like this: (x, y), where 'x' is the numerator, and 'y' is the denominator. For example, (2, 3) means 2/3. If the numerator is greater than the denominator (after the addition) you should extract the integer part and put it before the fraction. For example:
# fractions (((2, 3), (2, 3))) = "1 and 1/3", because the result will be - 4/3 (the numerator is greater than the denominator) and you can extract the integer part (1) and the remaining fraction (1/3).Make note that the conjunction 'and' is required if the result has both parts - the integer and the fraction.
# If the result doesn’t contain the fraction part and has only the integer - you should return it as the 'int'-type, not 'str'. If it doesn’t contain the integer part - just return it like a string 'N/D' where N - is the numerator and D - is the denominator.
# 
# 
# 
# Input:Fractions.
# 
# Output:The sum of fractions.
# 
# Precondition:
# 2 <= the amount of the fractions <= 10
# Positive fractions only.
# 
# 
# END_DESC

from fractions import Fraction


def add_fractions(data):
    score = sum(Fraction(x, y) for x, y in data)
    x, y = score.as_integer_ratio()
    if x < y:
        return str(score)
    elif x % y == 0:
        return x // y
    else:
        totals = x // y
        return f'{totals} and {score - totals}'

if __name__ == '__main__':
    print("Example:")
    print(add_fractions(((2, 3), (2, 3))))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert add_fractions(((2, 3), (2, 3))) == "1 and 1/3"
    assert add_fractions(((1, 3), (1, 3))) == "2/3"
    assert add_fractions(((1, 3), (1, 3), (1, 3))) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")