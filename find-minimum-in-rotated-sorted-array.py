'''
    My Solution: Create a left and right pointer and iterate through nums. If the right pointer is greater than left pointer value (nums is sorted), return the left most value. If nums is not 
    sorted, if the right side is sorted, set the right pointer to the middle (the smallest value is either at the middle or to the left side). If the right side is not sorted, the smallest 
    value is on the right side. 

    Test Cases: Observe all rotations for nums = [1, 2, 3, 4, 5]
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) / 2
            if nums[r] > nums[l]:
                return nums[l]
            else:
                if nums[mid] < nums[r]:
                    r = mid
                else:
                    l = mid+1
        return nums[l]