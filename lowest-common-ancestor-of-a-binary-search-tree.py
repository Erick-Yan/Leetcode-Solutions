'''
    My Solution: Since a binary tree has larger nodes to the right subtree and smaller nodes to the left, we can take advantage of that. Using recursion, we can find the smaller and larger node 
    between p and q. If the current node being traversed has a value that's in between the p and q, we return it. If it isn't, we continue iterating left if the current node is larger than both 
    p and q, else we iterate right.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        lower = p if p.val < q.val else q
        higher = p if p.val > q.val else q 
        if root.val >= lower.val and root.val <= higher.val:
            return root
        if higher.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p, q)