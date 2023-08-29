'''
goal - take a sudoku board and solve it
rule 1 - only numbers 1 to 9
rule 2 - each number appears 9 times
rule 3 - each number appears once per row - horizontally
rule 4 - each number appears once per row - vertically
rule 5 - the board is a 9 x 9 grid (81 spots) arranged in 3 3x3 grids
rule 6 - each number appears in each 3x3 grid once
'''
grid = [
11,12,13,14,15,16,17,18,19,
21,22,23,24,25,26,27,28,29,
31,32,33,34,35,36,37,38,39,
41,2,3,4,5,6,7,8,9,
51,2,3,4,5,6,7,8,9,
61,2,3,4,5,6,7,8,9,
71,2,3,4,5,6,7,8,9,
81,2,3,4,5,6,7,8,9,
91,2,3,4,5,6,7,8,99]

def row_check(grid):
    for i in range(0,81,1):
        
        print(grid[i])

row_check(grid)