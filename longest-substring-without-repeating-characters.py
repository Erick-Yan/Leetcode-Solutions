'''
    My Solution: Create a dictionary userChar to track the characters that've appeared. Iterate through the string. If the character has appeared before and is at an index greater than 
    or equal to that of start, move to 1 index past the previous instance when that character appeared. Else, update maxLength if the differences in indices is greater than the 
    current maxLength. Insert the character that's appeared and its index number within usedChar.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxLength = 0
        usedChar = {}
        for index,char in enumerate(s):
            if char in usedChar and start <= usedChar[char]:
                start = usedChar[char] + 1
            else:
                maxLength = max(maxLength, index - start + 1)
            usedChar[char] = index
            print(usedChar)
        return maxLength