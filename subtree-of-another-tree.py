'''
    My Solution: Iterate through the root nodes using DFS iterative approach. If the node value is the same as the subRoot value, leverage the recursion method from Same Tree to check if the node and 
    subRoot subtrees are equal. Return true if so, else, continue iterating through the root nodes.

    Faster Solution: Initially, check if the root and subTree are already matched. If the root value is null, return False. Recursively continue checking if the subTree is a sub tree of the 
    left or right sub trees of the root (using the same recursion method from Same Tree).

    Edge Cases: If root doesn't contain a tree; if subRoot doesn't contain a tree; if both don't contain a tree.

    Remember: A null subRoot compared to a root is still considered a sub tree.   
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEqual(self, root, subRoot):
        if not root and not subRoot:
            return True
        if (not root and subRoot) or (root and not subRoot):
            return False
        else:
            return root.val == subRoot.val and self.isEqual(root.left, subRoot.left) and self.isEqual(root.right, subRoot.right)
    
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not root and subRoot:
            return False
        if (root and not subRoot) or (not root and not subRoot):
            return True
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                if node.val == subRoot.val and self.isEqual(node, subRoot):
                    return True
                stack.append(node.left)
                stack.append(node.right)
                
        return False

    # Faster Solution
    def isMatch(self, s, t):
        if not(s and t):
            return s is t
        return (s.val == t.val and 
                self.isMatch(s.left, t.left) and 
                self.isMatch(s.right, t.right))

    def isSubtree(self, s, t):
        if self.isMatch(s, t): return True
        if not s: return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)