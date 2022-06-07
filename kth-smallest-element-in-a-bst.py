'''
    My Solution: Perform in-order DFS (iterative). Each time you pop a node from the stack (which collects all the left subtree elements), decrement the k value. If k reaches 0, it means 
    you've reached the kth smallest element.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = list()
        temp = root
        check = 0
        
        while stack or temp:
            while temp:
                stack.append(temp)
                temp = temp.left
            
            node = stack.pop(-1)
            check += 1
            if check == k:
                return node.val
            temp = node.right
            
        return -1