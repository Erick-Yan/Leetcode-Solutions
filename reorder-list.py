'''
    My Solution (above): Create a stack. After the fast node reaches the end, the slow node has arrived at the middle, which we can then begin to fill the stack.
    Iterate until the stack is empty. For each node from head, set the next node to be the most recent stack element, and that element's next node to be the next 
    node in head. If the stack is empty, set the stack's most recently popped node and its next node to be None (prevent linked list cycle) and break.

    Better Solution (below): Reverse the second half of the linked list after finding the middle node. Set the middle node to None (prevent linked list loop).
    Merge lists alternately.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        stack = []
        while slow.next:
            slow = slow.next
            if fast.next:
                fast = fast.next
            if fast.next:
                fast = fast.next
            if not fast.next:
                stack.append(slow)
        
        curr = head
        while stack:
            temp = curr.next
            popped = stack.pop()
            curr.next = popped
            if not stack:
                popped.next = None
                break
            popped.next = temp
            curr = temp
            
        return head        

class Solution:
    def reorderList(self, head):
        #step 1: find middle
        if not head: return []
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt    
        slow.next = None
        
        #step 3: merge lists
        head1, head2 = head, prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt