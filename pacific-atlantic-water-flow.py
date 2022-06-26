'''
    My Solution: Start by iterating through:
        1. The rows, from both the Pacific (first row) and the Atlantic (second row) oceans.
        2. The columns, from both the Pacific (first column) and the Atlantic (last column) oceans.
    Initialize 2 lists, one tracking the path tiles that connect to the Pacific and the other tracking path tiles connecting the Atlantic. Use a backtracking function (DFS). If the current tile's 
    index is out of bounds or if the current path tile's height is less than the previous path tile's height, return nothing (we are moving from the outer tiles towards the inside, and 
    in order for the water to flow from inside to outside, the inner tiles must be greater than or equal to the outer tiles). Else, add the current tile into either the Pacific or Atlantic 
    hashset and traverse the neighboring tiles. Finally, iterate through all the tiles again, for each, if they exist in both hashsets, append them into the return list.
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ret = []
        pVisited, aVisited = set(), set()
        
        def findPath(visited, i, j, prevHeight):
            if i < 0 or i == len(heights) or j < 0 or j == len(heights[i]) or heights[i][j] < prevHeight or (i, j) in visited:
                return
            visited.add((i, j))
            findPath(visited, i-1, j, heights[i][j])
            findPath(visited, i+1, j, heights[i][j])
            findPath(visited, i, j-1, heights[i][j])
            findPath(visited, i, j+1, heights[i][j])
        
        for m in range(len(heights)):
            findPath(pVisited, m, 0, heights[m][0])
            findPath(aVisited, m, len(heights[0])-1, heights[m][len(heights[0])-1])
        
        for n in range(len(heights[0])):
            findPath(pVisited, 0, n, heights[0][n])
            findPath(aVisited, len(heights)-1, n, heights[len(heights)-1][n])
            
        for j in range(len(heights)):
            for k in range(len(heights[j])):
                if (j, k) in pVisited and (j, k) in aVisited:
                    ret.append([j, k])
                    
        return ret  