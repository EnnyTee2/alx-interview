#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
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
