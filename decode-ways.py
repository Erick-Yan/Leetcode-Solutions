'''
    My Solution (Recursive DFS): We start at the first char. The number of combinations with it included is equal 
    to the number of combinations for the next char (findCombos(i+1)), thus we make our first recursive call. 
    If the current char and the next one has a value between 10 and 26, the number of combinations increase since 
    we are now looking for combinations that include the first 2 chars as a letter (findCombos(i+2)). For example:
        1123
        1: look for combos with 1 as letter (A)
        11: look for combos with 11 as letter (K)
    We can then update the combos (memoization) dictionary to remember the number of combination calculations so 
    we don't have to repeat calculations.
    The only number of combinations we are guaranteed to know is the last char, which only has one combination with 
    it starting (ex. for 1123, the number of combinations at the char 3 is 1).

'''

class Solution:
    def numDecodings(self, s: str) -> int:
        combos = {len(s): 1}
        
        def findCombos(i):
            if i in combos:
                return combos[i]
            if s[i] == "0":
                return 0
            ret = findCombos(i+1)
            if i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                ret += findCombos(i+2)
            combos[i] = ret
            return ret
        
        return findCombos(0)

'''
    My Solution (Dynamic Programming): Starting from the last char, we are confirmed to have only 1 combination 
    moving forwards. We iterate backwards keeping each calculated combination saved in the combos dictionary. The 
    approach is the same as the recursive solution when calculating for each # of combinations at each char.
'''

    def numDecodings(self, s: str) -> int:
        combos = {len(s): 1}
        
        for i in range(len(s)-1, -1, -1):
            if i in combos:
                continue
            if s[i] == "0":
                combos[i] = 0
                continue
            combos[i] = combos[i+1]
            if i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                combos[i] += combos[i+2]
        
        return combos[0]