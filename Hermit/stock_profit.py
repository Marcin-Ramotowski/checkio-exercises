#!/usr/bin/env checkio --domain=py run stock-profit

# You are a broker with a single chance to buy stock and sell stock. Having an array of prices, pick the best time to buy stock and sell stock to maximize the profit.
# 
# “short-selling” (sell first, buy later) is not allowed in this market.
# 
# Your profit is zero when it is impossible to get profit at all. The size of pricing can't be less than 2.
# 
# Input:Array of int. Stock prices.
# 
# Output:Int. Maximum possible profit.
# 
# 
# END_DESC

def stock_profit(stock: list) -> int:
    i, Min = min(enumerate(stock[:-1]), key=lambda x:x[1])
    Max = max(stock[i:])
    return max(Max - Min, 0)


print("Example:")
print(stock_profit([3, 1, 3, 4, 5, 1]))

assert stock_profit([2, 3, 4, 5]) == 3
assert stock_profit([3, 1, 3, 4, 5, 1]) == 4
assert stock_profit([4, 3, 2, 1]) == 0
assert stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]) == 4
assert stock_profit([1, 1, 1, 2, 1, 1, 1]) == 1
assert stock_profit([4, 3, 2, 1, 2, 1, 2, 1]) == 1
assert stock_profit([1, 1, 1, 1]) == 0

print("You are the best broker here! Click 'Check' to earn cool rewards!")