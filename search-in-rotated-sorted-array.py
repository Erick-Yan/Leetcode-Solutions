'''
    My Solution: Start with a left and right pointer. Iterate through nums. Calculate the middle index.
    If the left pointed value is less than the middle pointed value (left side is sorted), check if the 
    target is between the left and mid. If it is, set the right pointer to the middle (shrink nums), else, 
    look at the right side by setting the left pointer to 1 index past the middle. If the left side isn't 
    sorted, check to see if the right side is sorted. If the target is between the right side bounded values,
    move the left pointer to the middle (shrink the array right), else look at the left side only by setting 
    the right pointer to 1 index less than the middle. If the middle index holds the target, return the middle 
    index. 
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) / 2
            print(nums[l:r+1])
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                if target >= nums[l] and target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if target >= nums[mid] and target <= nums[r]:
                    l = mid
                else:
                    r = mid - 1
            
        return -1