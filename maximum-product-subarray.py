class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        currMax, currMin = 1, 1
        
        for num in nums:
            if not num:
                currMax, currMin = 1, 1
                continue
            tmp = currMax * num
            currMax = max(currMax*num, currMin*num, num)
            currMin = min(tmp, currMin*num, num)
            res = max(res, currMax)
            
        return res