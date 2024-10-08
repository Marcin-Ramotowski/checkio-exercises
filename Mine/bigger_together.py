#!/usr/bin/env checkio --domain=py run bigger-together

# Your mission here is to find a difference between the maximally positive and maximally negative numbers. Those numbers can be found by concatenating the given array of numbers.
# 
# Let’s check an example. If you have numbers 1,2,3, then 321 is the maximum number, and 123 - is the minimum. The difference between those numbers is 198. But if you have numbers 4, 3 and 12 then 4312 is the maximum number, and 1234 - is the minimum. As you can see, a simple order is not what we are looking for here.
# 
# Input:A list of positive integers.
# 
# Output:An integer.
# 
# Precondition:All elements of the list can't be less than 0
# The list can't be empty
# 
# 
# END_DESC

from typing import List

def bigger_together(numbers: List[int]) -> int:
    numbers = list(map(str,numbers))
    digits = ''.join(numbers)
    k = len(digits)
    Mincandidates = [''.join(sorted(numbers)),''.join((sorted(numbers, key = lambda x: x if len(x)==k else x + (k -len(x)) * '9')))]
    Min = int(''.join(min(Mincandidates, key = lambda x: int(x))))
    Maxcandidates = [''.join(sorted(numbers,reverse=True)),''.join((sorted(numbers, key = lambda x: x if len(x)==k else x + (k -len(x)) * '9',reverse=True)))]
    Max = int(''.join(max(Maxcandidates, key = lambda x: int(x))))
    return Max - Min

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert bigger_together([1,2,3,4]) == 3087, "4321 - 1234"
    assert bigger_together([1,2,3,4, 11, 12]) == 32099877, "43212111 - 11112234"
    assert bigger_together([0, 1]) == 9, "10 - 01"
    assert bigger_together([100]) == 0, "100 - 100"
    print (bigger_together([420,42,423]))
    print('Done! I feel like you good enough to click Check')