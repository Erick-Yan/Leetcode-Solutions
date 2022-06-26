'''
    My Solution: Prioritize the most frequent task by creating a max heap from the tasks list. Create a queue that will track tasks that have been completed and the next time period they can 
    be taken up again. Iterate until the heap or the queue is empty. Increment the time on each iteration. If the heap isn't empty, pop the most frequent item and decrement its frequency. If 
    the remaining frequency is not 0, append it into the queue along with the next time which the task can be performed (pushed back into the heap). If the queue is not empty and the current 
    time is equal to the next time the first task in the queue can be performed, push that task back into the heap.
'''

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        tasks = Counter(tasks)
        heap = [-task for task in tasks.values()]
        heapq.heapify(heap)
        queue = list()
        time = 0
        
        while heap or queue:
            time += 1
            
            if heap:
                task = 1+heapq.heappop(heap)
                if task:
                    queue.append([task, time+n])
            if queue and queue[0][1] == time:
                task = queue.pop(0)
                heapq.heappush(heap, task[0])
                
        return time