#!/usr/bin/env checkio --domain=py run changing-direction

# Given a list of integers.  Your task in this mission is to find how many times sorting directions was changed in the given list.
# 
# Changing the sorting direction is when the last number in the list 1, 2, 3 is followed by a number < 3.
# 
# 
# 
# Input:List.
# 
# Output:Int.
# 
# Precondition:the list is non-empty
# 
# the elements in the list is positive integers
# 
# 
# 
# 
# END_DESC

def changing_direction(elements: list) -> int:
    isAsc = True
    x = 0
    last = elements[0]
    for item in elements[1:]:
        if (item < last and isAsc) or (item > last and not isAsc):
            x += 1
            isAsc = not isAsc
        last = item
    return x


print("Example:")
print(changing_direction([1, 2, 3, 4, 5]))

assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")