#!/usr/bin/env checkio --domain=py run swap-nodes

# Your task is to swap elements of the list (Iterable) pairwise. If you are given a list of 4 elements, then your function should return the same list, only in it the first and second elements are interchanged, as well as the third and fourth.
# 
# If there isn’t a paired amount of elements, then leave the last unpaired element in its place. An empty list should remain empty.
# 
# Input:Iterable.
# 
# Output:Iterable.
# 
# 
# END_DESC

from itertools import chain
swap_nodes = lambda x:list(chain.from_iterable(list(zip(x[1::2],x[0::2])))) if len(x) % 2 == 0 else list(chain.from_iterable(list(zip(x[1::2],x[0::2])))) + [x[-1]]