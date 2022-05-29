'''
    My Solution: Divide & Conquer. Iterate through each pair of linked lists, merge each pair (using the strategy from merge-two-sorted-lists.py), and append 
    them into a new list called merged_lists. Then continue iterating until all list pairs have been merged (only 1 list remains in merged_lists).

    Time Complexity: 0(n*log(k))
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def merge_lists(self, l1, l2):
        new_head = temp = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 if l1 else l2
        return new_head.next
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                merged_lists.append(self.merge_lists(l1, l2))
            lists = merged_lists
        
        return lists[0]