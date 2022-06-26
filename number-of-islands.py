'''
    My Solution: Iterate through each grid tile and use a backtracking function (DFS). Return nothing if the index is out of bounds or the grid tile isn't 1. Else, mark the current tile as 0 
    (to mark it as part of an island and that its been traversed) and traverse the neighboring tiles until the current island has been covered. If the current tile (that initiated the DFS) 
    is 1, we run the backtracking function and increment the return value.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        
        for row in range(len(grid)):
            for num in range(len(grid[row])):
                def isIsland(i, j):
                    if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[i])-1 or grid[i][j] != "1":
                        return
                    grid[i][j] = "0"
                    isIsland(i-1, j)
                    isIsland(i+1, j)
                    isIsland(i, j-1)
                    isIsland(i, j+1)
                    
                if grid[row][num] == "1":
                    isIsland(row, num)
                    ret += 1
                    
        return ret