'''
    My Solution: Iterate through each board tile. Perform a backtracking function (DFS). If the current word index is out of bounds, return true (it means we've completed the word). If the 
    board indices are out of bounds of if the current tile isn't equal to the word character, return False. Else, we mark the current tile as 0 (to mark it as traversed and prevent any tiles in 
    the path continuation from crossing the same path) and traverse the 
    neighboring tiles to see which path would form the word. We then revert the original tile value to allow any following starting tiles being traversed to cross that path.
'''

class Solution(object):
    def find(self, wordIndex, word, i, j, board):
        if wordIndex > len(word) - 1:
            return True
        if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[i]) - 1 or word[wordIndex] != board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = 0
        foundOption = self.find(wordIndex+1, word, i-1, j, board) or self.find(wordIndex+1, word, i+1, j, board) or self.find(wordIndex+1, word, i, j-1, board) or self.find(wordIndex+1, word, i, j+1, board)
        board[i][j] = tmp
        return foundOption
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.find(0, word, i, j, board):
                    return True
        return False