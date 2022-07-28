'''
    My Solution: Work backwards with memoization. The last square has 1 path to get to it.
    The number of paths square to its left can take to get to the last square is equal to 
    the number of paths at the last square. Same for the square above the last square. In 
    otherwards, we track and mark the number of paths that can arrive at the final square 
    at each square.
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for i in range(m+1)]
        dp[m-1][n] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = dp[i][j+1]+dp[i+1][j]
                
        return dp[0][0]