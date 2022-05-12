'''
    My Solution: Create a hashmap to track te number of appearances a specific character makes. Create a left and right pointer, both starting at the first element of s. 
    Iterate through s. Increment the hashmap key value depending on which character appears. For each element, find the largest occurring character in the hashmap. If the difference 
    between the current substring length - largest occuring character is less than or equal to k (the number of replacements, in this case the least occuring character, is less 
    than or equal to k), update longest based on the max substring length. If the difference is greater than k, slide the window (left pointer) to the right, and decrement the character 
    that gets removed from the previous substring in the hashmap.
'''

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start = trail = longest = 0
        charac = dict()
        while trail < len(s):
            charac[s[trail]] = charac.get(s[trail], 0) + 1
            higher = max(charac.values())
            if (trail - start + 1) - higher <= k:
                longest = max(longest, trail - start + 1)
            else:
                charac[s[start]] = charac.get(s[start], 0) - 1
                start += 1
            trail += 1
                
        return longest