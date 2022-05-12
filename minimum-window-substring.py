'''
    My Solution: Create one hashmap called model to get the number of occurrences of each character in t. Create another hashmap called extras to track the number of extras that 
    appear for those characters in t. Iterate through s. Increment the right pointer until it arrives at a character within t (to efficiently start at a potential window by eliminating 
    all characters that don't appear in t). If the right point is less than the left pointer, set it equal to the left. If the current character pointed by the right pointer is in t, 
    decrement its key within the model hashmap. If we've already decremented all of its values in model, the current character is extra, thus increment its key in the extras hashmap. 
    If the sum of the values in the model hashmap is 0 (we've encountered all the characters in t), we can update the minimum window substring if its length is less than 
    the current minimum substring length or the minimum substring is empty. Since we will be sliding the window to the right, we are removing the left-most character from the new 
    substring, thus, if the left-most character is in t, increment its value within the model hashmap. Since that left-most character could've appeared more times than required, we 
    iterate the model hashmap and if a character's value isn't 0 and there exist extras of that character in the extras hashmp, decrement the value of that character in both model 
    and extras (since the character has appeared more times than necessary, the extras hashmap allows us the maintain the minimum window condition). Increment the left pointer.

    Better Solution:
'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        min_win = ""
        l = r = 0
        model = dict()
        extras = dict()
        for char in t:
            model[char] = model.get(char, 0) + 1
            extras[char] = 0
        while r < len(s):
            if s[l] not in t and l < len(s) - 1:
                l += 1
                continue
            if r < l:
                r = l
            if s[r] in t:
                if model[s[r]] != 0: model[s[r]] -= 1
                else: extras[s[r]] += 1
            while sum(list(model.values())) == 0:
                if len(min_win) > r - l + 1 or not min_win:
                    min_win = s[l:r+1]
                if s[l] in t: model[s[l]] += 1
                for key, value in model.items():
                    if model[key] != 0 and extras[key]:
                        model[key] = value - 1
                        extras[key] -= 1
                l += 1
            r += 1
                
        return min_win