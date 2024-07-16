#!/usr/bin/env checkio --domain=py run x-o-referee

# Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players    (X and O) who take turns marking the spaces in a 3×3 grid.    The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal rows (NW-SE and    NE-SW) wins the game.
# 
# But we will not be playing this game. You will be the referee for this games results. You are given a result of a    game and you must determine if the game ends in a win or a draw as well as who will be the winner. Make sure to    return "X"    if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".
# 
# 
# 
# A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.
# 
# Input:A game result as a list of strings (unicode).
# 
# Output:"X", "O" or "D" as a string.
# 
# Precondition:
# There is either one winner or a draw.
# len(game_result) == 3
# all(len(row) == 3 for row in game_result)
# 
# 
# END_DESC

from typing import List
from itertools import chain

def checkio(grid: List[str]) -> str:
    chars = ('O', 'X')
    columns = [[row[i] for row in grid] for i in range(3)]
    diagonals = [[grid[i][i] for i in range(3)], [grid[i][2-i] for i in range(3)]]

    def result(part):
        for char in chars:
            if part.count(char) == 3:
                return char

    for row in chain(grid, columns, diagonals):
        score = result(row)
        if score:
            return score   
    return 'D'