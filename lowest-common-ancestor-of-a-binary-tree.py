'''
    My Solution: In a while loop, perform a DFS search for p or q on the left and right subtree within the recursive function searchSubTree. If the left and right subtree contain p and q, the 
    current node is the lowest common ancestor. If the current node is p or q, the current node is also the lowest common ancestor. If only one subtree has both p and q (left or right), set 
    root to equal that node and continue iterating.

    Better Solution: Perform the recursion in the lowestCommonAncestor function itself.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchSubTree(self, root, p, q):
        if not root:
            return None
        if root.val == p.val:
            return p
        if root.val == q.val:
            return q
        left = self.searchSubTree(root.left, p, q) 
        right = self.searchSubTree(root.right, p, q)
        if left and right:
            return root
        return left if left else right
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ret = None
        
        while not ret:
            left = self.searchSubTree(root.left, p, q)
            right = self.searchSubTree(root.right, p, q)
            if (left and right) or root.val == p.val or root.val == q.val:
                return root
            root = left if left else right            
            
        return ret

    # Faster Solution
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left = right = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
            