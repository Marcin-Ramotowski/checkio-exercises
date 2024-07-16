#!/usr/bin/env checkio --domain=py run compress-list

# A given list should be "compressed" in a way so, instead of two (or more) equal elements, staying one after another, there is only one in the result Iterable (list, tuple, iterator ...).
# 
# 
# 
# Input:List.
# 
# Output:"Compressed" Iterable (list, tuple, iterator ...).
# 
# 
# END_DESC

from typing import Iterable


def compress(items: list) -> Iterable:
    if len(items) < 2:
        return items
    output = [items[0]]
    checker = items[0]
    for i in range(1, len(items)):
        el = items[i]
        if el != checker:
            checker = el
            output.append(el)
    return output