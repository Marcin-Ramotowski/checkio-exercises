#!/usr/bin/env checkio --domain=py run aggregate-and-count

# You have a list of values where each element is a list of two values. First is a name and the second one is counter.
# 
# What you need to do is to aggregate those values into a dict, which is easy, you can simply use function disc for that. But, name is not unique, so if you find more that one elements with the same name, you should sum their counters in the aggregated dict.
# 
# Input:List of list of two elelemnts - str and int.
# 
# Output:Int.
# 
# 
# END_DESC

def aggregate_and_count(items: list) -> dict:
    scores = {}
    for key, val in items:
        scores.update({key: scores.get(key, 0)+val}) 
        # second parameter in method 'get' is default
        # default means value that will be returned when key will not be found in the dictionary
    return scores


print("Example:")
print(aggregate_and_count([["a", 1], ["b", 2], ["c", 3], ["a", 5]]))

assert aggregate_and_count([["a", 1], ["b", 2]]) == {"a": 1, "b": 2}
assert aggregate_and_count([["a", 1], ["a", 2]]) == {"a": 3}
assert aggregate_and_count([["a", 1], ["b", 2], ["c", 3], ["a", 5]]) == {
    "a": 6,
    "b": 2,
    "c": 3,
}
assert aggregate_and_count([["a", 1]]) == {"a": 1}

print("The aggregation is done! Click 'Check' to earn cool rewards!")