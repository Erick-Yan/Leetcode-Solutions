'''
    My Solution: Use recursive approach. For each root node of each subtree, we need to determine:
        1. The largest path sum from the left subtree.
        2. The largest path sum from the right subtree.
        3. The largest path sum that connects the left, middle, and right sides.
        4. If the current root node is from a subtree, we must return the largest path from itself without splitting both left and right direction.
    We need to find the max of the left and right subtree first. If the largest path is less than 0, we can avoid adding it to the root node by determining the max between its return value and 
    0. We can update the maxSum value if the previous maxSum is less than the path sum of the left, middle, and right subtree nodes. We then return the max value between the sum of the root and 
    left max or root and right max (depending on which path is greater) to the stack below in the scenario that the current root node is a subtree root node.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxSum = [root.val]
        
        def findMax(root):
            if not root:
                return 0
            leftMax = max(findMax(root.left), 0)
            rightMax = max(findMax(root.right), 0)
            
            maxSum[0] = max(maxSum[0], root.val + leftMax + rightMax)
            return max(root.val + leftMax, root.val + rightMax)
        
        findMax(root)
        return maxSum[0]