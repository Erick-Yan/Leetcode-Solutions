'''
    My Solution: Create a fast and slow pointer. If the fast pointer catches up to the slow pointer (they equate), there exists a loop. If the fast pointer arrives 
    at a NULL value, there is no loop.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False