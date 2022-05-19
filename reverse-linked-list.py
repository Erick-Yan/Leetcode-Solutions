'''
    My Solution: Create two pointers, one previous and one current. Iterate through the linked list. Save the current pointer's next pointer into temp, set current pointer's next pointer at 
    previous. Then update previous as the new current and current as temp (original next pointer).
'''

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head
        
        while curr: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev