'''
    My Solution: Perform in-order DFS search. For each node popped from the stack into the ret_list, check if it is greater than the last node that was appended. If not, return false (this 
    means the current node value is less than the previous).)
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = list()
        ret_list = list()
        temp = root
        
        while stack or temp:
            while temp:
                stack.append(temp)
                temp = temp.left
            node = stack.pop(-1)
            if ret_list and node.val <= ret_list[-1]:
                return False
            ret_list.append(node.val)
            temp = node.right
            
        return True