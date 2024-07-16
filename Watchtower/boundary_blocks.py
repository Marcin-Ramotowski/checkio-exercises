#!/usr/bin/env checkio --domain=py run boundary-blocks

# This mission is like a subset ofVisibilities.
# 
# You are given a list of strings as grid.Empty cells will be represented by '.', and the blocks - by 'X'.Blocks are not adjacent to each other vertically and horizontally.
# 
# One area consists of empty cells that are adjacent to each other vertically and horizontally.You must return the coordinates of the blocks that make the boundary.
# 
# Input:A list of strings.
# 
# Output:An iterable of tuples of two integers (In row, column order).
# 
# Preconditions:3 ≤ len(grid) ≤ 203 ≤ len(grid[0]) ≤ 20all(set(row) <= {'.', 'X'} for row in grid)
# 
# 
# END_DESC

from typing import List, Tuple, Iterable


def boundary_blocks(grid: List[str]) -> Iterable[Tuple[int]]:

    return []


if __name__ == '__main__':
    assert set(boundary_blocks(['..X',
                                '.X.',
                                'X..'])) == {(0, 2), (1, 1), (2, 0)}, '#1 3x3'
    assert set(boundary_blocks(['...',
                                '.X.',
                                'X..'])) == set(), '#2 3x3'
    assert set(boundary_blocks(['X.X.',
                                '.X..',
                                '..X.',
                                '....'])) == {(0, 0), (0, 2), (1, 1)}, '#3 4x4'

    print('The local tests are done. Click on "Check" for more real tests.')