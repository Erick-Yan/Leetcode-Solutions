# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def switchRoots(self, root):
        if not root:
            return root
        else:
            root.left, root.right = root.right, root.left
            self.switchRoots(root.left)
            self.switchRoots(root.right)
            return root
    
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        root = self.switchRoots(root)
        return root