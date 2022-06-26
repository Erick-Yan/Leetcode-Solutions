'''
    My Solution: Perform BFS using a queue. Initialize a clone dictionary to store all the cloned nodes. For each node popped from the queue, iterate through their neighbor. If the neighbor node 
    doesn't exist in the clone dictionary, create a cloned node using its node.val and add it to the queue. Add the cloned neighbor node to the neighbor list of the initial popped node.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        queue = [node]
        cloneDict = {node.val: Node(node.val)}
        
        while queue:
            node1 = queue.pop()
            copyNode = cloneDict[node1.val]
            
            for neighbor in node1.neighbors:
                if neighbor.val not in cloneDict:
                    queue.append(neighbor)
                    cloneDict[neighbor.val] = Node(neighbor.val)
                copyNode.neighbors.append(cloneDict[neighbor.val])
        
        return cloneDict[node.val]
        