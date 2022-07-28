'''
    My Solution: Same approach as House Robber, except since we can't rob the last and first house together, we can only consider 
    two options:
        - nums from the 2nd to last value.
        - nums from the 1st to the 2nd last value.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.robHouse(nums[:-1]), self.robHouse(nums[1:]))

    def robHouse(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for n in nums:
            tmp = max(prev+n, curr)
            prev = curr
            curr = tmp

        return curr