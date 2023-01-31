#!/usr/bin/python3
""" LockBoxes Interview Challenge """


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    """
    box_len = len(boxes)  # get total number of boxes
    keys = boxes[0][:]  # initialised list to store availabe keys
    box_list = {}  # dictionary to keep track of each box's unlock status
    count = 0  # unlock cycle counter
    pending = 0  # tracker for unopened boxes
