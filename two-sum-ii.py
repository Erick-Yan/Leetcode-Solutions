'''
    My Solution: Create two pointers pointing to both ends of numbers. Iterate through numbers. If the elements pointed at add up to the target, return the indices + 1 each. 
    If the elements add up to a value greater than the target, decrement the right pointer, else, increase the left pointer.
'''

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] > target:
                right -= 1
                continue
            left += 1
            