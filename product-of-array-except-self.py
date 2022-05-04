'''
    My Solution: Leverage the prefix and postfix. Notice that for each element's index in the answer list, the value is the product of the to its left and right.
    We can obtain answer list by calculating the product of the elements to the left and right of each element using the prefix and postfix, respectively. 
    For the prefix, we start with 1 since the value to the left of the first element doesn't exist, so we set it 1. 
    Calculate the incrementing product through each of nums's elements from the left and append into the answer list. 
    For the postfix, we start with 1 again since the vlue to the right of the last element doesn't exist. 
    Calculate the incrementing product through each of num's elements and multiply that product with the elements in the answer list both from the right.
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        prod = 1
        for num in nums:
            answer.append(prod)
            prod *= num
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= prod
            prod *= nums[i]
        return answer