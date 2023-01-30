#!/usr/bin/python3
"""" LockBoxes Interview Challenge """


def canUnlockAll(boxes):
    """ This function checks if all the boxes can be unlocked """
    
    box_len = len(boxes)
    keys = boxes[0]
    box_list = {}
    count = 0
    pending = 0

    while count < box_len - pending:
        x = 1
        while x < box_len:
            if x in keys:
                box_list[f'{x}'] = True
                for key in boxes[x]:
                    if key not in keys:
                        keys.append(key)
            else:
                box_list[f'{x}'] = False
                pending += 1
            x += 1
        count += 1
        if pending == 0:
            break
  
    for status in box_list.values():
        if status == False:
            return False
 
    return True
