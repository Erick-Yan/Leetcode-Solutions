'''
    My Solution: Create a modified list that contains sublists that include the coordinate distance from origin, the first, and the second coordinate value. Create a heap using those values. 
    Iterate through the heap until we've reached the kth heap node, each one being appended into a return list.
'''

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dists = [[(coord[0]**2)+(coord[1]**2), coord[0], coord[1]] for coord in points]
        heapq.heapify(dists)
        ret = []
        
        while len(ret) != k:
            coords = heapq.heappop(dists)
            ret.append([coords[1], coords[2]])
            
        return ret