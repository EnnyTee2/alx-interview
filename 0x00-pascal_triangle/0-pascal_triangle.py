#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal triangle (PT) of n:
        Returns an empty list if n <= 0
        assumes n will be always an integer
    """
    master = [] # list of lists to hold the entire pascal triangle
    count = 0 # counter variable

    if (n <= 0):
        return master

    while count < n:
        if count == 0: # Step 1 of pascals triangle
            temp = [1] # temporary list for hold the tem
            master.append(temp)
        elif count == 1: # Step 2 of pascals triangle
            temp = [1, 1]
            master.append(temp)
        else: # other higher steps
            outer = count - 1 # return index of previous step
            length = len(master[outer]) # length of preceding step of PT
            temp = [] # empty the temporary holding list
            
            for i in range(length + 1): # looping for the next step of PT  
                if (i == 0 or i == length): # if index is first or last
                    temp.append(1) # insert the left and right bounding 1s
                if (i <= length - 2): # Get the next PT set from the previous set
                    temp.append(master[outer][i] + master[outer][i + 1]) # algo

            master.append(temp) # append the current list to the main Triangle list.
        count += 1 # increment the counter
    return master
