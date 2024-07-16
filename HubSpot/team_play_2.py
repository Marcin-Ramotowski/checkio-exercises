#!/usr/bin/env checkio --domain=py run team-play-2

# Two teams of robots are playing the game ofcut-or-bend. 	The rules of the game are very simple:The team that has processed more details than its opponent is		a winner.A detail is considered to be processed if it is either bent or cut.Each robot can perform both bending and cutting, but during the game  		it can perform only one of two functions.Each team consists of N players, K of them must be occupied with cutting. 		All the rest must be occupied with bending.Suppose you are the coach of one of these teams. You are given two lists 	of positive integers both of size N representing stats of your team. The i-th value 	in the first list is the number of details that can be cut by the i-th member of 	the team during the game. Similarly, the i-th value in the second list is the number 	of details which can be bent by the i-th member of the team during the game. Knowing 	the value of K, calculate the maximum score which can be obtained by your team.
# 
# Input:Three arguments. Two lists of integers of equal size representing team's stats. 	An integer - a number of team's members that have to be occupied with cutting.
# 
# Output:An integer - the maximum score which can be obtained by the team.
# 
# 
# END_DESC

from typing import List, Iterable

def max_score(cut: List[int], bend: List[int], k: int) -> int:
    pairs = list(zip(cut, bend))
    pairs = sorted(pairs, key=sub, reverse=True)
    score = 0
    for i in range(len(pairs)):
        if i < k:
            score += pairs[i][0]
        else:
            score += pairs[i][1]
    return score

def sub(pair: Iterable[int]) -> int:
    return pair[0] - pair[1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(max_score([4, 2, 1], [2, 5, 3], 2))

    assert max_score([4, 2, 1], [2, 5, 3], 2) == 10, "Your team can do better."
    assert max_score([7, 1, 4, 4], [5, 3, 4, 3], 2) == 18, "Bet you can improve this."
    assert max_score([5, 5, 5], [5, 5, 5], 1) == 15, "Almost there!"
    print("Coding complete? Click 'Check' to earn cool rewards!")