#!/usr/bin/python3
'''rotate 2D matrix'''


def rotate_2d_matrix(matrix):
    '''rotates a 2d matrix 90° clockwise
    Returns: Nothing '''
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            # save topleft  value
            topLeft = matrix[top][left + i]
            # move bottom left to top left
            matrix[top][left + i] = matrix[bottom - i][left]
            # move bottom right to bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # move top right to bottom right
            matrix[bottom][right - i] = matrix[top + i][right]
            # move top left to top right
            matrix[top + i][right] = topLeft
        right -= 1
        left += 1


"""def rotate_2d_matrix(matrix):
    """ Rotates a n x n matrix by 90 degrees """
     import copy
    matcopy = copy.deepcopy(matrix)
    fwd = 0
    current = 0
    revrs = len(matrix) - 1
    for start in range(len(matrix)):
        while fwd < len(matrix):
            matrix[start][fwd] = matcopy[revrs][current]
            revrs -= 1
            fwd += 1
        current += 1
        fwd = 0
        revrs = len(matrix) - 1
"""
