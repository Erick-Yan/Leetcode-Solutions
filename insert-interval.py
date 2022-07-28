class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        ret = []
        i = 0
        
        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][-1]:
                ret.append(intervals[i])
                continue
            if newInterval[-1] < intervals[i][0]:
                ret.append(newInterval)
                return ret + intervals[i:]
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[-1], intervals[i][-1])]
            
        ret.append(newInterval)
            
        return ret
            