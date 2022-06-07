'''
    My Solution: Perform BFS search. For each level, initialize a level_queue list to append each node from that level (the one that's ultimately popped). After iterating through that level's 
    nodes, append the level_queue list into the ret_queue list to finalize that level's nodes.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        queue = [root]
        ret_queue = list()
        
        while queue:
            level_queue = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level_queue.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret_queue.append(level_queue)
                
        return ret_queue
        