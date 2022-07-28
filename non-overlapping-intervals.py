'''
    My Solution: The trick here is to always take the interval pair with the shortest range:
    ex. [1, 2] vs [1, 10]. [1, 10] takes up a larger interval and has a higher chance of 
    overlapping with the next interval, thus we take [1, 2]. Ensure you sort the interval 
    list in the beginning.

    Time Complexity: O(nlogn).
'''

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        prevEnd = intervals[0][-1]
        ret = 0
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < prevEnd:
                prevEnd = min(intervals[i][-1], prevEnd)
                ret += 1
                continue
            prevEnd = intervals[i][-1]
            
        return ret