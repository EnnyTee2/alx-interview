#!/usr/bin/python3

def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n:
        Returns an empty list if n <= 0
        assumes n will be always an integer
    """
    
    master = []
    temp = []
    count = 0
    
    while count <= n:
        if count == 0:
            temp = [1]
            master.append(temp)
            
        elif count == 1:
            temp = [1, 1]
            master.append(temp)
        else:
            outer = count-1
            length = len(master[outer])
            temp = []
            for i in range(length+1):
                if (i == 0 or i == length):
                    temp.append(1)
                if (i <= length-2):
                    temp.append(master[outer][i] + master[outer][i + 1])

            master.append(temp)
        count += 1
    return master
