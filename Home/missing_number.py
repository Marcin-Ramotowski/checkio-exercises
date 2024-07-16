#!/usr/bin/env checkio --domain=py run missing-number

# You are given a sequence of integers, which are elements of arithmetic progression - the difference between the consecutive elements is constant.    But this sequence is unsorted and one element is missing...good luck!
# 
# 
# 
# Input:Listof integers(int).
# 
# Output:An integer(int).
# 
# Examples:
# 
# assert missing_number([1, 4, 2, 5]) == 3
# assert missing_number([2, 6, 8]) == 4
# Preconditions:length of sequence > 2;missing element is always between two elements in sequence.
# 
# 
# END_DESC

def missing_number(items: list[int]) -> int:
    items.sort()
    differences = [items[i + 1] - items[i] for i in range(len(items) - 1)]
    index, max_diff = max(enumerate(differences), key=lambda x: x[1])
    return items[index] + max_diff // 2


print("Example:")
print(missing_number([1, 4, 2, 5]))

assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")