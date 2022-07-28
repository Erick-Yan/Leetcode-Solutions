'''
    My Solution: Create a ret list holding the first interval pair. First sort the interval 
    list by the first element. Iterate through the rest of the interval list. If the current 
    pair intersects with the last interval pair in ret, merge the interval by replacing the 
    last elementing in the pair with the max value between the ret pair and current pair. If 
    the current pair doesn't intersect, just append into ret.

    Time Complexity: O(nlogn) due to the sorted() in the beginning.
'''

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        ret = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if ret[-1][-1] >= intervals[i][0]:
                ret[-1][-1] = max(ret[-1][-1], intervals[i][-1])
                continue
            ret.append(intervals[i])
            
        return ret