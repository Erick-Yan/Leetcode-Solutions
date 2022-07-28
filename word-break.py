'''
    My Solution: Implement a Trie and add the dictionary words into it. We will utilize a bottom-up approach along 
    with memoization. Start by creating a list marking each position of the string s and one more being True. The 
    True at the end marks the end of a word. We start iterating through the s backwards. If a character is the start 
    of a dictionary word, we iterate to the end of s to ensure that's the case (using Trie isWord property to 
    check). If the entire string that's been iterated through using nodes is a word and the index past the current 
    one is marked True in the dp, we mark the initial character index in dp as True:
        "catsandog" ["cats", "and", "dog"]
        dp = [False, False, False, False, False, False, False, True, False, False, True]
        When we arrive at "d", we iterate until the end, notice its a word and that the index past it in dp is True 
        thus we mark dp[indexOf("d")] as True. 
        When we arrive at "a", its also the start of a dictionary word, but once we iterate until "d", even though its 
        a word, it's also a part of another word "dog", thus the word break would not work.
'''

class Trie(object):
    def __init__(self):
        self.nodes = {}
        self.isWord = False
    def addWord(self, word):
        currNode = self
        for char in word:
            if char not in currNode.nodes:
                currNode.nodes[char] = Trie()
            currNode = currNode.nodes[char]
        currNode.isWord = True

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        root = Trie()
        for word in wordDict:
            root.addWord(word)
        
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
            
        for i in range(len(s)-1, -1, -1):
            currNode = root
            for j in range(i+1, len(s)+1):
                if s[j-1] not in currNode.nodes:
                    break
                currNode = currNode.nodes[s[j-1]]
                if currNode.isWord and dp[j]:
                    dp[i] = True
                    break
                      
        return dp[0]