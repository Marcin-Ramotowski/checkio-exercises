#!/usr/bin/env checkio --domain=py run when-k-is-enough

# Given a list of items, some of which may be duplicated, create and return a new Iterable that is otherwise the same asitems, but only up tokoccurrences of each element are kept, and all occurrences of that element after those firstkare discarded. Note also the counterintuitive but still    completely legitimate edge case ofk == 0that has a well defined answer of an empty list!
# 
# Input:A list and an integer.
# 
# Output:List or another Iterable (tuple, iterator, generator).
# 
# Examples:
# 
# assert list(remove_after_kth([42, 42, 42, 42, 42, 42, 42], 3)) == [42, 42, 42]
# assert list(remove_after_kth([42, 42, 42, 99, 99, 17], 0)) == []
# assert list(remove_after_kth([1, 1, 1, 2, 2, 2], 5)) == [1, 1, 1, 2, 2, 2]
# This task is taken from the course CCPS 109 Computer Science I, as taught byIlkka Kokkarinen.
# 
# 
# END_DESC

from typing import Iterable


def remove_after_kth(items: list, k: int) -> Iterable:
    counter = {}
    score = []
    if k <= 0:
        return []
    for item in items:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
        if counter[item] <= k:
            score.append(item)
    return score


print("Example:")
print(list(remove_after_kth([42, 42, 42, 42, 42, 42, 42], 3)))

assert list(remove_after_kth([42, 42, 42, 42, 42, 42, 42], 3)) == [42, 42, 42]
assert list(remove_after_kth([42, 42, 42, 99, 99, 17], 0)) == []
assert list(remove_after_kth([1, 1, 1, 2, 2, 2], 5)) == [1, 1, 1, 2, 2, 2]

print("The mission is done! Click 'Check Solution' to earn rewards!")