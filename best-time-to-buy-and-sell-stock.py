'''
    My Solution: Create a current low pointer and a trailing pointer. Iterate through prices. If the value pointed by the trailing pointer is larger than the current low pointer value, 
    and if their difference is greater than the current max profit, replace the current max profit. Increment the trailing pointer. If the trailing pointer value is less than the 
    current low pointer value, set the current low pointer value to the trailing pointer value and update the trailing pointer value to be one index ahead of the current low pointer.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        curr_low, it = 0, 1
        max_prof = 0
        while it < len(prices):
            if prices[it] > prices[curr_low]:
                prof = prices[it] - prices[curr_low]
                if prof > max_prof:
                    max_prof = prof
                it += 1
                continue
            curr_low = it
            it += 1
        return max_prof