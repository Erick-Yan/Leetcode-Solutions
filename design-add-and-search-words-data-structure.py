'''
    My Solution: Use a recursive DFS approach to the search method. Iterate through the word's characters in a for loop. If the char is ".", we iterate through potential TrieNode 
    that has keys that might equal the current character through a recursive call of the DFS search where we pass the next word's char and the current TrieNode's keys (values).
    If the char is not ".", we approach it in the same manner as the Implement Trie Prefix Tree way. After iterating through the entire for loop, we check if the we've reached 
    the end of the word by checking if the TrieNode word property is True.
'''

class TrieNode:
    def __init__(self):
        self.children = {} # a : TrieNode
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
        
    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        
        return dfs(0, self.root)