'''
    My Solution: A trie is a prefix tree, which like a hashmap, stores various words from the English dictionary, but the nodes allow us to take advantage of prefixes and move 
    in a specific direction depending on which word we are trying to find out of the all the words that use that prefix. We also want to mark the end of each word with a # node. 
    For the insert operation, it graphically looks like the following: Insert(apple) => {a:{p:{p:{l:{e:#}}}}}, where each character has its own dictionary to dictate which 
    direction to go depending on the word we are trying to insert/find.

    Note: The prefix can be the entire word; When searching for a word, the end of the word in the trie must have a #.
'''

class Trie(object):

    def __init__(self):
        self.node = dict()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        currNode = self.node
        for char in word:
            if char not in currNode:
                currNode[char] = {}
            currNode = currNode[char]
        currNode['#'] = '#'

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        currNode = self.node
        for char in word:
            if char not in currNode:
                return False
            currNode = currNode[char]
        if '#' in currNode:
            return True
        return False

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        currNode = self.node
        for char in prefix:
            if char not in currNode:
                return False
            currNode = currNode[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)