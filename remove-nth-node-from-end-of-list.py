'''
    My Solution: Create 2 pointers. The first pointer iterates normally, the second pointer starts iterating when the space between itself and the first is 
    greater than or equal to n (since we are looking to remove the nth node from the end - first pointer). Also iterate a pointer that keeps track of the pointer 
    that points at the node behind the second pointer (since we want to equate its next value to be the second pointer).
    After the first pointer reaches the end, if the nth pointer to be removed is the head pointer, set head to the next node in the list. If the pointer behind the 
    second pointer is not a NULL value, set its next value to be the second pointer's next value.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        prev = end = head
        prev_behind = None
        space_between = 0
        while end.next:
            end = end.next
            space_between += 1
            if space_between >= n:
                prev_behind = prev
                prev = prev.next
        
        if prev == head:
            head = head.next
        if prev_behind:
            prev_behind.next = prev.next
            
        return head