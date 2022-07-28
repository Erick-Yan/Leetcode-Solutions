'''
    My Solution: Consider the Fibonnaci sequence.
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 0
        for i in range(n):
            tmp = a + b
            b = a
            a = tmp

        return a
        