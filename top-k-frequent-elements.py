'''
    My Solution: Create a dictionary to track the number of occurences for each unique number. 
    Create a list of lists with size equal to the size of nums, where each list's index represents the number of occurences, and inside each list are the unique numbers from nums 
    that appear as many times as the index. 

    TC: O(n)
    SC: O(n)
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count_dict = dict()
        count_list = [[] for i in nums]
        return_list = []
        
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        for key, val in count_dict.items():
            count_list[val-1].append(key)
        for num_list in count_list[::-1]:
            return_list = return_list + num_list            
            if len(return_list) == k:
                return return_list