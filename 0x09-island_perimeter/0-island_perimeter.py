#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    ""Return the perimeter
    of the island described in grid:""
    perimeter = 0
    glen = len(grid)
    zlen = len(grid[0])

    for i in range(0, glen):
        if i == 0 or i == glen - 1:  # top or bottom border
            for j in range(0, zlen):
                if grid[i][j] == 1:  # land found on border
                    if grid[i][j+1] == 0 && grid[i][j-1] == 0:
                        perimeter += 3
                    while j > 0 && j < zlen -1:
                        if grid[i][j-1] == 0 && grid[i][j+1] == 1:
                            perimeter += 2
                        if grid[i][j-1] == 1 && grid[i][j+1] == 1:
                            perimeter += 1


        else:
            for j in range(0, zlen):
                if j == 0 or j == zlen - 1:  # left or right border
                    if grid[i][j] == 1:  # land found on border
                        
                else:
                    if grid[i][j] == 1:  # land found in cell
                        # The if blocks below detects
                        # if the cell is surrounded by water
                        if grid[i][j+1] == 0:
                            perimeter += 1
                        if grid[i][j-1] == 0:
                            perimeter += 1
                        if grid[i+1][j] == 0:
                            perimeter += 1
                        if grid[i-1][j] == 0:
                            perimeter += 1
    return perimeter


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
