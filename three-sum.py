'''
    My Solution: Iterate through nums (sorted). For each element, perform a two sum for the rest of the 
    list (after that element) using left and right pointers. If the three sum is less than zero, 
    increment the left pointer. If the three sum is greater than zero, decrement the right pointer. 
    If the three sum is equal to zero, append the triplet into a return list and increment the left 
    pointer. IMPORTANT: consider the last case where you increment the left pointer, but the following 
    element is the exact same as the previous (hint: while loop until it's a different value or until 
    left pointer reaches right pointer).
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    ret.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return ret