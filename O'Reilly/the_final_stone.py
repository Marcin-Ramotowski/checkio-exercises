#!/usr/bin/env checkio --domain=py run the-final-stone

# You have a list of stones with different weights. The result of hitting two stones will be a new stone with a weight difference between the two stones.
# 
# 
# 
# Your goal is to find the weight of the final stone. If no stones left, the result is 0.
# 
# The algorith is very simple:
# 
# get the two biggest stones in the batchhit and get the resulting stoneput the resulting stone back in the batch.For the Speedy category, you can think about your solution for a million stones
# 
# Input:List of stones as list of ints
# 
# Output:Int.
# 
# 
# END_DESC

import bisect


def final_stone(stones: list[int]) -> int:
    if not stones:
        return 0
    stones.sort()
    while len(stones) > 1:
        print(stones)
        a, b = stones[-2], stones[-1]
        stones = stones[:-2]
        new = b - a
        if new:
            bisect.insort(stones, new)
    return max(stones) if stones else 0

print('Example:')
print(final_stone([1,2,3]))

assert final_stone([3, 5, 1, 1, 9]) == 1
assert final_stone([1, 2, 3]) == 0
assert final_stone([1, 2, 3, 4]) == 0
assert final_stone([1, 2, 3, 4, 5]) == 1
assert final_stone([1, 1, 1, 1]) == 0
assert final_stone([1, 1, 1]) == 1
assert final_stone([1, 10, 1]) == 8
assert final_stone([1, 10, 1, 8]) == 0
assert final_stone([]) == 0
assert final_stone([1]) == 1
assert final_stone([10, 20, 30, 50, 100, 10, 20, 10]) == 10

print("The mission is done! Click 'Check Solution' to earn rewards!")