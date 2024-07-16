#!/usr/bin/env checkio --domain=py run making-change

# Nicola is taking a much needed vacation.  He'll be backpacking around some lesser-known countries.  Each has its own unique currency.
# 
# When making purchases, Nicola would like to use the minimum number of coins possible.  For example, Outer Leftopia has coins with denomination 1, 3, and 5 shillings.  He wants to buy a souvenir that costs 13 shillings.  He can do that using two 5 shilling coins and one 3 shilling coin.
# 
# You can assume Nicola has access to an infinite number of coins of each denomination.  (He has a large bank account and access to an ATM).
# 
# Input:Two arguments. The first argument is an int: the price of the purchase.      The second is a list of ints: the denominations of available coins.
# 
# Output:int. The minimum number of coins Nicola can use to make the purchase.    If the price cannot be made with the available denominations, returnNone.
# 
# Precondition:Inputs are all positive integers.
# 
# 
# END_DESC

def checkio(k, denoms):
    a = len(denoms)
    infinity = 2147483647
    table = [0]
    for i in range(1, k+1):
        table.append(infinity)
    for n in denoms:
        for j in range(0, k-n+1):
            if table[j] < infinity:
                if table[j] + 1 < table[j + n]:
                    table[j + n] = table[j] + 1
    score = table[k]
    if score == infinity:
        return None
    else:
        return score

if __name__ == '__main__':
    print("Example:")
    print(checkio(8, [1, 3, 5]))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(8, [1, 3, 5]) == 2
    assert checkio(12, [1, 4, 5]) == 3
    print('Done')