'''
    My Solution: Use a recursive approach. Notice that the first element in the preorder list is the root node. The root node, when found inside the inorder list: if you look on both sides of 
    the list with the root node in the middle, it reveals the root node's left and right subtree. This is the case for every node inside the inorder list. We can iterate through the preorder 
    list nodes. For each recursive iteration, we can find the index of the preorder node inside the inorder list. We then set the current node's left node to be middle of the subset of the 
    inorder list from 0 until the current node index inside the inorder list (which represents its left subtree). The same approach is done for the current node's right node.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, prestart, preorder, inorder):
        if prestart > len(preorder) - 1 or preorder[prestart] not in inorder:
            return None
        
        root = TreeNode(preorder[prestart])
        root_index = inorder.index(preorder[prestart])
        
        root.left = self.helper(prestart+1, preorder, inorder[0:root_index])
        root.right = self.helper(prestart+root_index+1, preorder, inorder[root_index+1:])
        
        return root
        
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(0, preorder, inorder)