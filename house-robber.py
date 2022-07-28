'''
    My Solution: Leverage dynamic programming. Let's start with the list [2, 7, 9, 3, 1]. For every house, we want to track the largest amount resulting from the start to the previous house (curr) 
    and the largest amount that lies from the start to the house prior to the previous house (prev: to track the largest amount from the previous non-adjacent house). We start with 2 pointers 
    curr and prev which are both 0 starting before the first house. Let's say we are at 7. We want to know check whether the prev pointer, which stores the largest amount up to the house prior to 2,
    added to 7 (since we can only rob non-adjacent houses) is greater than the curr pointer value, which stores the largest amount up to the 2.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for n in nums:
            tmp = max(prev+n, curr)
            prev = curr
            curr = tmp

        return curr