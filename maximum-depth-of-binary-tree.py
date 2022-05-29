# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # DFS Recursion Approach: check the tree root's left and right subtrees recursively and update the count everytime.
    def recursiveCount(self, root, count):
        if not root:
            return count
        else:
            count += 1
            left_count = self.recursiveCount(root.left, count)
            right_count = self.recursiveCount(root.right, count)
            return max(left_count, right_count)
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = self.recursiveCount(root, 0)
        
        return count

    # DFS Iterative Approach: create a stack. While the stack isn't empty, iterate through each node. If it isn't null, update the res value if depth is greater, and append the left and right 
    # node and the updated depth into the stack.
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        res = 0
        
        while stack:
            node, depth = stack.pop()
        
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

    # BFS Iterative Approach: create a queue. While the queue is not empty, iterate through the nodes, and for each, if they have a left or/and right node, append into the queue.
    # Each time you append the left or/and right node for every node in the queue, you reached another level in the tree (level-order search), so increment the level count.
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        level = 0
        queue = deque([root])
        
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
            
        return level