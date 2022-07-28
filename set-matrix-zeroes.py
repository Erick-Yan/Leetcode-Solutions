'''
    My Solution: Iterate through the entire matrix and mark which row and column needs 
    to be zeroed. Then, iterate through the entire matrix again and convert the rows 
    that should be zero to zero. Do the same for the columns.
'''

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rowsZero, colsZero = [False] * len(matrix), [False] * len(matrix[0])
    
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not matrix[i][j]:
                    rowsZero[i] = True
                    colsZero[j] = True
                    
        for i in range(len(rowsZero)):
            if rowsZero[i]:
                for j in range(len(colsZero)):
                    matrix[i][j] = 0
                    
        for i in range(len(colsZero)):
            if colsZero[i]:
                for j in range(len(rowsZero)):
                    matrix[j][i] = 0

        return matrix

'''
    Alternative Solution (O(1)): Iterate through the matrix. If the current square is 
    0, mark the leftest square on the same row to 0 and the top most square on the same 
    column to 0. If the current square is 0 and is from the first row, set rowZero to True.
    We need this to determine whether we need to set the entire first row to 0 or not.
    Then, iterate through the entire matrix again. When we encounter a square that's 0, 
    check if the adjacent topmost and leftmost squares are set to 0. If so, set it to 
    0. Lastly, check if we need to zero the first column and row.
'''

    def setZeroes(self, matrix: List[List[int]]) -> None:
        # O(1)
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # determine which rows/cols need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0