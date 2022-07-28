'''
    My Solution: Leverage an adjacency list, which contains the course as the key and the value as a list of prerequisites. 
    
    {
        0: [1],
        1: [2],
        2: [0]
    }

    Iterate through each course (start from 0 to numCourses). Use DFS 
    approach. If the course has been visited, return False (since it indicates that the current course has appeared as a course and now a prerequisite, resulting in a cycle). If the course 
    has an empty prerequisites list, return True (since there are no more prerequisites to traverse). Else, add current course to visited set, iterate through its prerequisites calling the DFS 
    recursively. After, remove the current course from the visited set since we want the next course to be able to traverse it. Set the current course's prerequisite list to an empty list to 
    indicate that we don't need to traverse it anymore (since there's no cycle from that course).
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacencyList = {}
        for i in range(numCourses):
            adjacencyList[i] = []
        for crs, preq in prerequisites:
            adjacencyList[crs].append(preq)
        
        visited = set()
        def dfs(crs):
            print(crs)
            print(visited)
            if crs in visited:
                return False
            if not adjacencyList[crs] or crs > numCourses:
                return True
            visited.add(crs)
            for neighbor in adjacencyList[crs]:
                if not dfs(neighbor):
                    return False
            visited.remove(crs)
            adjacencyList[crs] = []
            return True
        
        for i in range(numCourses):
            if adjacencyList[i] and not dfs(i):
                return False
                    
        return True
        
        