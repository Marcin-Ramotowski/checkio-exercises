#!/usr/bin/env checkio --domain=py run the-cookie-monster

# The belovedCookie Monsterfrom Sesame Street has stumbled upon a table with sortedpilesof cookies, each pile a positive integer. However, the monomaniacal obsessiveness ofthe Countwho set up this crumbly fiesta has recently escalated to a whole new level of severity. The Count insists that these cookies must be eaten in thesmallest possible number of moves. Each move chooses one of theremaining pile sizesp, and removespcookies from every pile that contains at leastpcookies (thus eradicating all piles with exactlypcookies), and leaves all smaller piles as they were.
# 
# Since the Count also has an unhealthy obsession with order and hierarchies, he expects these moves to be done indecreasing orderof values ofp. This function should return the list of moves, that allows Cookie Monster to scarf down these cookies. If there are a few optimal sequences of moves, choose thelexicographically largestone. Look at the example for[1, 2, 3, 4, 5, 6]input.
# 
# 
# 
# Input:Listof integers(int).
# 
# Output:Listof integers(int).
# 
# Examples:
# 
# assert cookie_monster([1, 2, 3]) == [2, 1]
# assert cookie_monster([1, 2, 3, 4, 5, 6]) == [4, 2, 1]
# assert cookie_monster([2, 3, 5, 8, 13, 21, 34, 55, 89]) == [55, 21, 8, 3, 2]
# assert cookie_monster([1, 10, 17, 34, 43, 46]) == [46, 34, 17, 9, 1]
# The above version of the Cookie Monster problem has been streamlined a bit to keep this problem simple enough to solve here. The more general problem formulation allows Cookie Monster to choose any subset of remaining piles, and remove the same freely chosen number of cookies from each pile in the chosen subset. Interested students can check out the article“On the Cookie Monster Problem”about the subtle complexities of the general problem formulation.
# 
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def cookie_monster(piles: list[int]) -> list[int]:
    # your code here
    return []


print("Example:")
print(cookie_monster([1, 2, 3]))

# These "asserts" are used for self-checking
assert cookie_monster([1, 2, 3]) == [2, 1]
assert cookie_monster([1, 2, 3, 4, 5, 6]) == [4, 2, 1]
assert cookie_monster([2, 3, 5, 8, 13, 21, 34, 55, 89]) == [55, 21, 8, 3, 2]
assert cookie_monster([1, 10, 17, 34, 43, 46]) == [46, 34, 17, 9, 1]

print("The mission is done! Click 'Check Solution' to earn rewards!")