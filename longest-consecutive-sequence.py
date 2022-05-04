'''
    My Solution: Sort and filter any duplicate values using set for nums. Iterate through nums 
    starting from the second element. Increment the counter (initial value set to 1 to count the 
    current element) by 1 if the element is equal to 1 + the previous element. If not, append the counter 
    value into the tracker list. Return the largest counter value in the tracker list.
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums = sorted(list(set(nums)))
        track = [1]
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                track.append(curr)
                curr = 1
                continue
            curr += 1
            if i == len(nums) - 1:
                track.append(curr)
        return max(track)