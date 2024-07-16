#!/usr/bin/env checkio --domain=py run median-of-three

# Given   an iterable of ints , create and return a new  iterable  whose first two elements are the same as in items, after which each element equals the median element in the sorted list of the three elements from the original list. Third element in sorted list is current position (position 2 and go on), first two elements are going before the third element in the original list.
# 
# 
# 
# Wait...You don't know what the "median" is? Go check out the separate"Median"mission on CheckiO.
# 
# Input:Iterable of ints.
# 
# Output:Iterable of ints.
# 
# The mission was taken from Python CCPS 109 Fall 2018. It’s being taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

from typing import Iterable


def median(numbers: list):
    numbers.sort()
    index = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[index]
    else:
        return (numbers[index] + numbers[index-1]) / 2


def median_three(els: Iterable[int]) -> Iterable[int]:
    numbers = []
    for i in range(len(els)):
        if i < 2:
            numbers.append(els[i])
        else:
            number = median([els[i], els[i-1], els[i-2]])
            numbers.append(number)
    return numbers


if __name__ == '__main__':
    print("Example:")
    print(list(median_three([1, 2, 3, 4, 5, 6, 7])))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
    assert list(median_three([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")