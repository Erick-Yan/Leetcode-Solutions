'''
    My Solution: Create a pointer tmp and set to an empty node. Set the head pointer to tmp. Iterate through both linked lists and set tmp value depending on which current linked list value is 
    smaller. Once one of the lists reached its end. Set the tmp's next value to whichever list still has values.
'''

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        tmp = ListNode()
        head = tmp
        while list1 and list2:
            if list1.val > list2.val:
                tmp.next = list2
                tmp = tmp.next
                list2 = list2.next
            elif list1.val <= list2.val:
                tmp.next = list1
                tmp = tmp.next
                list1 = list1.next
        
        tmp.next = list1 if list1 else list2
        
        return head.next