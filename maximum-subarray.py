'''
    My Solution: Iterate through nums. If the current num is greater than the current max 
    added with the current num, update the current max. If the current max is greater than 
    the max, update the max.
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = nums[0]
        currMax = nums[0]
        
        for i in range(1, len(nums)):
            currMax = max(nums[i], currMax+nums[i])
            if currMax > ret:
                ret = currMax
            
        return ret