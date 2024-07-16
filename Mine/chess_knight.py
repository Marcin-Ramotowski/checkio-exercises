#!/usr/bin/env checkio --domain=py run chess-knight

# Your friend loves chess very much, but he's not a strong player. You can help him by using your programming skills.
# If this mission is too simple for you, try another one from this set -The shortest Knight's path.
# 
# Your task is to write a function that can find all of the chessboard cells to which the Knight can move. The input data will consist of a start cell and the amount of moves that the Knight will make. There is only one figure on the board - your Knight.
# If the same cell appears more than once - do not add it again.You should return the list of all of the possible cells and sort them as follows:in alphabetical order (from 'a' to 'h') and in ascending order (from 'a1' to 'a8' and so on).
# 
# 
# 
# Input:A start cell, the number of moves.
# 
# Output:A list of all of the possible cells.
# 
# Precondition:
# 1 <= the number of moves <= 2
# 
# 
# 
# END_DESC

def chess_knight(start,moves):
    lexicon = {i+1:chr(97+i) for i in range(8)}
    cells = [start]
    cells2 = []
    for i in range(moves):
        for cell in cells:
            col, row = cell
            col = ord(col) - 96
            row = int(row)
            posses = [(col+1,row+2),(col-1,row-2),(col+1,row-2),(col-1,row+2),(col+2,row+1),(col-2,row-1),(col+2,row-1),(col-2,row+1)]
            posses = [ ''.join((lexicon[c],str(r))) for c,r in posses if 8 >= r > 0 and 8 >= c > 0]
            cells2 += posses
            cells = posses
    cells2 = sorted(set(cells2))
    return cells2