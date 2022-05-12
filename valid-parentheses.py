'''
    My Solution: Create a dictionary with the close brackets as the keys and open brackets as their values. Create a stack to track the open brackets that appear. Iterate through the 
    bracket string. If the brack is open, append it into the stack. Else, if there hasn't been an open bracket yet or the current close bracket isn't closing the correct open bracket, 
    return false. After iterating, if the stack is empty (meaning we've closed all brackets), return true, else false.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brac= { ")":"(", "]":"[", "}":"{" }
        stack = []
        
        for i in range(len(s)):
            if s[i] not in brac:
                stack.append(s[i])
            else:
                if not stack or stack[-1] != brac[s[i]]:
                    return False
                stack.pop()
        if not stack:
            return True
        return False