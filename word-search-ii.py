'''
    My Solution: Perform the same approach as Word Search 1, except we start with a Trie. The trie is built using the words that need to be verified. Iterate through each tile of the board. 
    Perform a backtracking function (DFS) on each board tile. If the board indices were out of bounds or the current tile has been visited or the current tile isn't a letter in the current 
    node's list of child nodes, return nothing. Else, we update the current node the that child node that equals the board tile, add the current board tile letter to the string builder. If 
    the current (updated) node has a isWord value of true, we append the string builder word into the return list. We then continue the backtracking function in the same manner as before.
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
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        ret, visited = list(), list()
        root = Trie()
        for word in words:
            root.addWord(word)
        
        def searchBoard(i, j, node, word):
            if i<0 or i==len(board) or j<0 or j==len(board[i]) or board[i][j] not in node.nodes or [i, j] in visited:
                return
            node = node.nodes[board[i][j]]
            word += board[i][j]
            if node.isWord:
                ret.append(word)
            visited.append([i, j])
            searchBoard(i-1, j, node, word)
            searchBoard(i+1, j, node, word)
            searchBoard(i, j-1, node, word)
            searchBoard(i, j+1, node, word)
            visited.remove([i, j])
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                searchBoard(i, j, root, "")
        
        return ret
        