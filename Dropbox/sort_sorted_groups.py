#!/usr/bin/env checkio --domain=py run sort-sorted-groups

# You are given a list of integers, and your goal is to perform the following steps:
# 
# Identify and group together all the sorted sequences within the list. A sorted sequence is a group of numbers that are arranged in either ascending or descending order.Sort the input list by these groups while preserving the relative order of elements within each group.Return the sorted list with the groups unpacked, meaning that the individual numbers from each group are in the final result, and their order reflects the sorted sequence within each group.For example, consider the input list[5, 1, 5, 0, 5]:
# 
# Group the numbers to obtain[[5, 1], [5, 0], [5]](three groups are identified).Sort the input list by groups while maintaining the relative order of elements within each group to get[[5], [5, 0], [5, 1]].Unpack the groups to obtain the final sorted list:[5, 5, 0, 5, 1].Let's look at another example in a view of a scheme:
# 
# 
# 
# Important Points:
# 
# When identifying sorted groups, adjacent equal numbers are considered part of the same group and keep previously detected order.To determine the sorting order for each group, look for the first different number beyond the initial equal numbers. The sorting order for each group is not determined once for the entire list.When building the groups, be greedy from the left, taking as many numbers as possible to create a distinct ordered sequence for each group.Good luck with your task!
# 
# Input:List of integers.
# 
# Output:List of integers.
# 
# Examples:
# 
# assert sorted_groups([]) == []
# assert sorted_groups([5]) == [5]
# assert sorted_groups([5, 1, 5, 0, 5]) == [5, 5, 0, 5, 1]
# assert sorted_groups([5, 5, 1]) == [5, 5, 1]
# 
# END_DESC

from itertools import chain


def sorted_groups(items: list[int]) -> list[int]:
    items2 = []
    group = []
    sorting_order = None
    for item in items:
        if not group:
            group.append(item)
            continue
        else:
            match sorting_order:
                case None:
                    if item > group[-1]:
                        sorting_order = 'asc'
                    elif item < group[-1]:
                        sorting_order = 'dec'
                    group.append(item)
                case 'asc':
                    if item >= group[-1]:
                        group.append(item)
                    else:
                        items2.append(group)
                        group = [item]
                        sorting_order = None
                case 'dec':
                    if item <= group[-1]:
                        group.append(item)
                    else:
                        items2.append(group)
                        group = [item]
                        sorting_order = None
    items2.append(group)
    items2.sort()
    return list(chain.from_iterable(items2))


print("Example:")
print(sorted_groups([5, 1, 5, 0, 5]))

assert sorted_groups([]) == []
assert sorted_groups([5]) == [5]
assert sorted_groups([5, 1, 5, 0, 5]) == [5, 5, 0, 5, 1]
assert sorted_groups([5, 5, 1]) == [5, 5, 1]

print("The mission is done! Click 'Check Solution' to earn rewards!")