'''
    My Solution: Sort the intervals. Create a minheap to track the upcoming end time of the 
    most recent meeting. Iterate through intervals. If the current interval's start time is 
    after the upcoming end time in minheap, this means we can replace the upcoming end time 
    with the current interval's end time. We don't need to add to the minheap, which also 
    represents the number of meeting rooms needed, since the latest meeting finished before 
    the current started, so we can use the same room. If the current interval has a starting 
    time before the upcoming ending time, we need a new room, hence we push it into the minheap.

    Time Complexity: O(nlogn)
'''

'''
    Alternative Solution (2 Pointers): We have a starting time and ending time list, each sorted.
    We iterate through the length of the lists. If the current start time is less than the 
    current end time, we need a room, so update our count and we shift our starting time 
    pointer by 1. If the current start time is greater than or equal to the current end time, 
    we shift our ending time pointer (update to the next ending time) and decrement our count.
    The minimum number of meeting rooms required is the max value count had.
'''

def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[0])
    heap = list()

    for i in range(len(intervals)):
        if heap and intervals[i][0] >= heap[0]:
            heapq.heappushpop(heap, intervals[i][1])
            continue
        heapq.push(heap, intervals[i][1])

    return len(heap)

