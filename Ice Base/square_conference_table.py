#!/usr/bin/env checkio --domain=py run square-conference-table

# You must combine several long desks to make a square conference table of the specified size.
# 
# The input values are the widths of the long desks (tuples of integer) and the side length of the table (integer).        The long desks have any width and their depth is always 1.The answer is the combinations of long desks that make the four sides of the table.        It must be a list of 4 tuples, each tuple being one or more integers.        The adjacent tuples in the resulting list to actually represent adjacent sides of the table.NOTE:Since there can be more than one correct answer, using a checker.All tests have correct answers.You don't always have to use up all the long desks.
# 
# Input:The long desks (a tuple of integers) and the side length of the table (a integer).
# 
# Output:The combinations of the long desks (a list of 4 tuples of integers).
# 
# square_conference_table((1, 2, 2, 3, 4, 4), 4) :ex_1:ex_2:[(4,), (3,), (2,1), (2,)][(4,), (2,), (4,), (2,)]Precondition:
# 
# len(long_desks) <= 20side_length <= 60Examples:
# 
# 
# from itertools import chain
# from collections import Counter
# from typing import Callable
# 
# 
# def checker(fn: Callable, ds: tuple[int, ...], s: int) -> bool:
#     result = fn(ds, s)
#     if Counter(chain(*result)) <= Counter(ds):
#         difs = [s - sum(r) for r in result]
#         return difs in ([1, 1, 1, 1], [2, 0, 2, 0], [0, 2, 0, 2]) or sorted(difs) == [0, 1, 1, 2]
#     return False
# 
# 
# assert checker(square_conference_table, (1, 2, 2, 3, 4), 4) is True
# assert checker(square_conference_table, (3, 3, 3, 3), 4) is True
# assert checker(square_conference_table, (1, 2, 2, 3, 3, 4, 5), 5) is True
# assert checker(square_conference_table, (1, 2, 3, 4, 5, 6), 6) is True
# 
# END_DESC

Desks = tuple[int, ...]
SquareTable = list[Desks, Desks, Desks, Desks]


def square_conference_table(desks: Desks, side_length: int) -> SquareTable:
    # your code here
    return []


print("Example:")
print(square_conference_table((2, 2, 3, 4, 5), 5))

# These "asserts" are used for self-checking
from itertools import chain
from collections import Counter
from typing import Callable


def checker(fn: Callable, ds: tuple[int, ...], s: int) -> bool:
    result = fn(ds, s)
    if Counter(chain(*result)) <= Counter(ds):
        difs = [s - sum(r) for r in result]
        return difs in ([1, 1, 1, 1], [2, 0, 2, 0], [0, 2, 0, 2]) or sorted(difs) == [
            0,
            1,
            1,
            2,
        ]
    return False


assert checker(square_conference_table, (1, 2, 2, 3, 4), 4) is True
assert checker(square_conference_table, (3, 3, 3, 3), 4) is True
assert checker(square_conference_table, (1, 2, 2, 3, 3, 4, 5), 5) is True
assert checker(square_conference_table, (1, 2, 3, 4, 5, 6), 6) is True
assert checker(square_conference_table, (1, 2, 3, 4, 5, 6, 7), 8) is True
assert checker(square_conference_table, (1, 2, 3, 4, 5, 6, 7, 8), 10) is True

print("The mission is done! Click 'Check Solution' to earn rewards!")