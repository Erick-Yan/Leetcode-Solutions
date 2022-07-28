'''
    My Solution: Approach is similar to Course Schedule, but we also check that there shouldn't be any isolated nodes and edges from the main tree. We create the same adjacency list to traverse 
    through each node in the entire graph. We leverage the same DFS approach. If the current node has been visited, return False (since this will create a loop in the tree, which would 
    invalidate the tree). Else, we add the current node to the visited set and iterate through its neighboring nodes. In the iteration, if we arrive at a neighboring node that's equal to the 
    previous node, we skip it (since this will cause us to iterate recursively in a cycle), else, we check recursively call the DFS function for the neighboring node. At the end, we return 
    if the initial DFS call is true and the length of visited set is equal to the number of nodes (to ensure the initial DFS traversal covered all nodes, hence, there's aren't any isolated 
    nodes). We don't traverse every node as done in Course Schedule because we want to see from the first node (0), are we able to traverse across all the other nodes.
'''

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        if not n:
            return True         
        adj = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True 
        
        return dfs(0, -1) and n == len(visit)