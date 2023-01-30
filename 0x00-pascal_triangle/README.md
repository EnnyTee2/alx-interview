# 0x00. Pascal's Triangle

Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

    * Returns an empty list if n <= 0
    * You can assume n will be always an integer
    
## Example Code: 

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

print_triangle(pascal_triangle(5))

## OUTPUT 
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
