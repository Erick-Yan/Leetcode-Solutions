'''
    My Solution: Create a new list containing all the negative values of the stone weights (to mimic a max heap using python's minheap library). Iterate through the heap until its length is <= 
    1. During each iteration, we pop out the 2 largest weighted stones and push back into the heap their weight differences (0 if both stones are equal weight since they destroy each other). 
    We then check if the heap still contains a stone weight after its weight elimination process. If it does, we return that final stone weight, else return 0.
'''

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones_neg = [stone * -1 for stone in stones]
        heapq.heapify(stones_neg)
        
        while len(stones_neg) > 1:
            stone1 = heapq.heappop(stones_neg) * -1
            stone2 = heapq.heappop(stones_neg) * -1
            heapq.heappush(stones_neg, (stone1 - stone2) * -1)
        
        if stones_neg:
            return heapq.heappop(stones_neg) * -1
        return 0