class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if not w in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if not w in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            if not w in curr.children:
                return False
            curr = curr.children[w]
        return True
        