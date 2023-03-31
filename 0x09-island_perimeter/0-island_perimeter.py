#!/usr/bin/python3
"""Defines a function for measuring island perimeter."""


def island_perimeter(grid):
    """Return the perimiter of an island.
    The grid represents water by 0 and land by 1.
    Args:
        grid (list): A list of list of integers representing an island.
    Returns:
        The perimeter of the island defined in grid.
    """
    width = len(grid[0])
    height = len(grid)
    edges = 0
    size = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                size += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    edges += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    edges += 1
    return size * 4 - edges * 2


"""def island_perimeter(grid):
    '''gets the perimeter of island in grid
       Returns: int (perimeter)
    '''
    if grid == [] or grid == [[]]:
        return 0
    leng = len(grid)
    lenc = len(grid[0])
    perimeter = 0

    try:
        for x in range(1, leng):
            for i in range(1, lenc):
                if grid[x][i] == 1:
                    if grid[x][i-1] == 0:
                        perimeter += 1
                    if grid[x][i+1] == 0:
                        perimeter += 1
                    if grid[x-1][i] == 0:
                        perimeter += 1
                    if grid[x+1][i] == 0:
                        perimeter += 1
    except Exception as e:
        return 0
    return perimeter
"""
