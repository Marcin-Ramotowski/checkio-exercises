#!/usr/bin/env checkio --domain=py run filling

# This mission is an adaptation of the "Filling" game (fromSimon Tatham's Portable Puzzle Collection).	If you are lost or just want to play, the game is availablehere.
# 
# You have a rectangular grid with digits. You have to fill the grid with digits	in such a way that each connected region (diagonally separated squares are not	adjacent) of identical digits has an area equal to that common digit.
# 
# Empty cells are represented by zeros.
# 
# Note:It is possible that the solution grid contains regions	without that none of its cells were given in the input grid	(such as the 3s and a 1 in the first example).
# 
# Input:A list of lists of integers.
# 
# Output:A list/tuple of lists/tuples of integers.
# 
# To play the puzzles / tests yourself:12345678910111213141516
# 
# Preconditions:All puzzles have one and only one solution.3 ≤ len(grid) ≤ 25 and 3 ≤ len(grid[0]) ≤ 25.all(len(row) == len(grid[0]) for row in grid).
# 
# 
# END_DESC

from typing import List


def filling(grid: List[List[int]]) -> List[List[int]]:
    return grid


if __name__ == "__main__":

    def checker(input_grid, result):
        # 1) Check types.
        assert isinstance(result, (tuple, list)) and all(
            isinstance(row, (tuple, list))
            and all(isinstance(n, int) and 0 <= n <= 9 for n in row)
            for row in result
        ), ("The result must be a list of lists of ints between 0 and 9.", [])
        # 2) Check sizes.
        nrows, ncols = len(input_grid), len(input_grid[0])
        assert len(result) == nrows and all(len(row) == ncols for row in result), (
            "The result must have the same sizes as the input grid.",
            [],
        )
        # 3) Check if there is any forbidden change from the input grid.
        changes = [
            (i, j)
            for i, row in enumerate(input_grid)
            for j, n in enumerate(row)
            if n != 0 and result[i][j] != n
        ]
        assert not changes, (
            "You must not change non-empty cells in the given grid.",
            changes,
        )
        # 4) Check if there is any empty cell in the result grid.
        empties = [
            (i, j) for i, row in enumerate(result) for j, n in enumerate(row) if n == 0
        ]
        assert not empties, ("There are %d empty cells." % len(empties), empties)
        # 5) Check if the grid is filled the right way.
        unvisited = {(i, j) for i in range(nrows) for j in range(ncols)}
        while unvisited:
            start = i, j = min(unvisited)
            stack, cells, expected = [start], [], result[i][j]
            while stack:
                pos = i, j = stack.pop()
                if pos not in unvisited:
                    continue
                unvisited.remove(pos)
                cells.append(pos)
                for neighbor in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                    x, y = neighbor
                    if 0 <= x < nrows and 0 <= y < ncols:
                        if neighbor in unvisited and result[x][y] == expected:
                            stack.append(neighbor)
            assert len(cells) == expected, (
                "Zone at %s should have %d elements, not %d."
                % (start, expected, len(cells)),
                sorted(cells),
            )

    def grid2url(grid):
        url = "https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/filling.html"
        ncols, nrows = len(grid[0]), len(grid)
        line = "".join(str(digit) for row in grid for digit in row)
        for i in range(26)[::-1]:
            line = line.replace("0" * (i + 1), chr(ord("a") + i))
        return f"{url}#{ncols}x{nrows}:{line}"

    GRIDS = (
        [[0, 2, 0], [0, 0, 2], [0, 1, 0]],
        [
            [0, 0, 2, 1, 0],
            [3, 3, 0, 0, 4],
            [0, 0, 0, 4, 4],
            [2, 2, 3, 0, 0],
            [5, 0, 0, 0, 0],
        ],
        [
            [1, 0, 1, 0, 1, 4, 0, 0],
            [3, 0, 2, 3, 0, 0, 0, 4],
            [0, 0, 0, 1, 0, 0, 5, 1],
            [4, 0, 1, 3, 0, 1, 0, 0],
            [5, 0, 0, 0, 0, 0, 0, 8],
            [0, 0, 1, 2, 1, 0, 0, 0],
        ],
    )

    for grid in GRIDS:
        result = filling([row[:] for row in grid])
        try:
            checker(grid, result)
        except AssertionError as checker_error:
            error_message, wrong_cells = checker_error.args[0]
            print("You failed on the grid %dx%d:" % (len(grid), len(grid[0])))
            print(error_message)
            if not wrong_cells:
                print(result)
            else:
                print("Positions of the wrong cells:", wrong_cells)
                for row in result:
                    print(*row)
                if "change non-empty cells" not in error_message:
                    print(
                        "If you want to solve your own incomplete grid manually, you can use this link:"
                    )
                    print(grid2url(result))
            break
    else:
        print('Click on "Check" for more tests.')