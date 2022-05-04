'''
    My Solution: Use 2 pointers that start from opposite ends of the string. Iterate the string. 
    If the current character is not alphanumeric, increment the pointer and continue the loop. If the 
    characters that each pointer points to aren't equal, return False.
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return true
        s = s.lower()
        left_pnt = 0
        right_pnt = len(s) - 1
        while left_pnt <= right_pnt:
            if not s[left_pnt].isalnum():
                left_pnt += 1
                continue
            if not s[right_pnt].isalnum():
                right_pnt -= 1
                continue
            if s[left_pnt] != s[right_pnt]:
                return False
            left_pnt += 1
            right_pnt -= 1
        return True