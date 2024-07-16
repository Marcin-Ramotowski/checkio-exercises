#!/usr/bin/env checkio --domain=py run sort-except-zero

# Sort the numbers in an array. But the position of zeros should not be changed.
# 
# Input:A List.
# 
# Output:An Iterable (tuple, list, iterator ...).
# 
# 
# END_DESC

from typing import Iterable


def except_zero(numbers: list) -> Iterable:
    length = len(numbers)
    indexes = []
    numbers2 = []
    x = 0
    while numbers.count(0) != 0:
        i = numbers.index(0) + x
        indexes.append(i)
        numbers.remove(0)
        x += 1
    numbers.sort()
    k = 0
    for j in range(length):
        if j in indexes:
            numbers2.append(0)
        else:
            numbers2.append(numbers[k])
            k += 1
    return numbers2


if __name__ == '__main__':
    print("Example:")
    print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
    assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
    assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
    assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
    assert list(except_zero([0, 0])) == [0, 0]
    print("Coding complete? Click 'Check' to earn cool rewards!")