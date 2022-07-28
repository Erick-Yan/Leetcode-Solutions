'''
    My Solution: Ensure intervals don't overlap (refer to Non-overlapping Intervals).
'''

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x: x[0])
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prevEnd:
                return False
            prevEnd = intervals[i][1]

        return True