#!/usr/bin/env checkio --domain=py run best-stock

# You are given the current stock prices. You have to find out which stocks cost more.
# 
# Input:The dictionary where the market identifier code is a key and the value is a stock price.
# 
# Output:The market identifier code (ticker symbol) as a string.
# 
# Preconditions:All the prices are unique.
# 
# 
# END_DESC

best_stock = lambda x: max(x.items(), key = lambda x:x[1])[0]