'''
    My Solution: Create a list to track list members that've already appeared. Return false if a number already exists in that list, else continue iterating. 
    Return true if the list has been iterated through.

    Better Solution: Check if the list length is equal to the list length of its set.
'''
class Solution(object):
    def containsDuplicate(self, nums):
        appeared = []
        for i in nums:
            if i in appeared:
                return True
            appeared.append(i)
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        return not (sorted(list(set(nums))) == sorted(nums))