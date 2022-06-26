'''
    My Solution: Create a heap with first k nodes (to ensure the first node in the heap is the kth smallest). Iterate through the rest of the nodes from the nums list. For each node, push it in 
    and pop out the smallest one. This will ensure that largest k nodes are left in the heap and that the first one is the kth largest.
'''

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n_list = nums[:k]
        heapq.heapify(n_list)
        
        for num in nums[k:]:
            heapq.heappush(n_list, num)
            heapq.heappop(n_list)
        return n_list[0]

'''
    My Solution: Use quick sort recursively. Choose a random element in the list and create 2 lists:
        1. Sublist of elements greater than the random element.
        2. Sublists of elements equal to the random element.
        3. Sublists of the elements less than the random element.
    If k is less than the last index of the sublist 1, the kth largest element resides in it so we recursively call the function with sublist 1. 
    If k is greater than the first index of sublist 3, the kth largest element resides in it so we recursively call the function with sublist 2 and update the k value.
    If k is between indices of the options above, it means the kth largest element is the random element selected at the beginning, so we return it.
'''

def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return
        p = random.choice(nums)
        l, m, r = [x for x in nums if x > p], [x for x in nums if x == p], [x for x in nums if x < p]
        nums, i, j = l+m+r, len(l), len(l)+len(m)
        return self.findKthLargest(nums[:i], k) if k <= i else self.findKthLargest(nums[j:], k-j) if k > j else nums[i]