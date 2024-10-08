#!/usr/bin/env checkio --domain=py run sort-array-by-element-frequency

# Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.
# 
# Input:Iterable
# 
# Output:Iterable
# 
# Precondition:elements can be ints or strings
# 
# The mission was taken from Python CCPS 109 Fall 2018. It's being taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

def frequency_sort(items):
    checkedItems = []
    Dict = {}
    for item in items:
        if item not in checkedItems:
            frequency = items.count(item)
            Dict[item] = frequency
            checkedItems.append(item)
    sortedDict = sorted(Dict.items(), key=lambda x: x[1], reverse=True)
    i, k = [0,0]
    while i < len(sortedDict):
        newValue = sortedDict[i][0]
        repeats = sortedDict[i][1]
        j = 0
        while j < repeats:
            items[k] = newValue
            j += 1
            k += 1
        i += 1
    return items

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")