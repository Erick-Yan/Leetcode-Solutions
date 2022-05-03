'''
    My Solution: Iterate through list. For each element, check if it exists in the diff list. 
    If not, append the difference value of the target and current element into the diff list. 
    If it does exist, return the index of the element in the diff list and the current index in the nums list that we're on.
'''

class Solution(object):
    def twoSum(self, nums, target):
        diff = []
        for i, num in enumerate(nums):
            if num not in diff:
                diff.append(target - num)
                continue
            return [diff.index(num), i]