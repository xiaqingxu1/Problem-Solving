class TrieNode:
    def __init__(self):
        self.childrens = [None] * 26
        self.end = False
        
class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not curr.childrens[i]:
                curr.childrens[i] = TrieNode()
            
            curr = curr.childrens[i]
        curr.end = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not curr.childrens[i]:
                return False
            curr = curr.childrens[i]
        return curr.end == True

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if not curr.childrens[i]:
                return False
            curr = curr.childrens[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)