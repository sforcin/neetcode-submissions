from typing import List


def in_bounds(grid: List[List[int]], r: int, c: int) -> bool:
    # takes in a grid (2x2 matrix), 2 integers 
    #rows and columns. r is index of a row, c is the index of a column
    #we need to check if theyre within bounds of the grid 
    #to check the columns, we do len(grid)
    #to check the rows, we do len(grid[0])
    rows = len(grid)
    cols = len(grid[0])
    if r> rows or c > cols or c<0 or r<0:
        return False
    else:
        return True
    pass


# do not modify below this line
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 2))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, 3))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 4))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, -1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1, 3))
