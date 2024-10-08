#!/usr/bin/env checkio --domain=py run frequency-sorting

# Your mission is to sort the list by the frequency of numbers included in it. If a few numbers have an equal frequency - they should be sorted according to their natural order. For example: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5]
# 
# 
# 
# Input:Chaotic list of numbers.
# 
# Output:The list of numbers in which they are sorted by their frequency.
# 
# Precondition:
# array length <= 100
# max number <= 100
# 
# 
# END_DESC

def frequency_sorting(items):
    checkedItems = []
    Dict = {}
    for item in items:
        if item not in checkedItems:
            frequency = items.count(item)
            Dict[item] = frequency
            checkedItems.append(item)
    Dict = dict(sorted(Dict.items()))
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
    print(frequency_sorting([1, 2, 3, 4, 5]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
    assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [4, 4, 4, 3, 3, 11, 11, 7, 13], "Not sorted"
    assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [10, 10, 21, 21, 55, 55, 99, 99], "Reversed"
    print("Coding complete? Click 'Check' to earn cool rewards!")