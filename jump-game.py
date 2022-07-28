'''
    My Solution: Iterate backwards. Initialize a goal variable with the last index of the 
    list. If the previous index can reach it (index + value at index >= goal), we update the 
    goal. If the goal arrives at the first index, the route indicates we can jump to the end.
'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal = len(nums) - 1
        
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0

'''
    My Solution: Create a var m to track the further you can jump at your current position. 
    If at the current index, you can make progress further than the previous jump, update the 
    var m. If the current index passes where the previous jump can reach, you've reached a 0.
'''

    def canJump(self, nums):
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True