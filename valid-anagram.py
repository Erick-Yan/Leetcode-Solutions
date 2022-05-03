'''
    My Solution: Sort both strings alphabetically, then check if they're equal.
'''

class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)