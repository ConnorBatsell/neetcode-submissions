class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True
        
    def search(self, word: str) -> bool:
        def dfs(idx, node):
            curr = node
            for i in range(idx, len(word)):
                c = word[i]
                if c ==".":
                    for a in curr.children.values():
                        if dfs(i+1, a):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.word
        return dfs(0,self.root)
            

        
                