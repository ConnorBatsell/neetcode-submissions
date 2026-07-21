class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        
    def search(self, word: str) -> bool:
        def dfs(node, idx):
            curr = node
            for i in range(idx, len(word)):
                if word[i]=='.':
                    for a in curr.children.values():
                        if dfs(a, i+1):
                            return True
                    return False
                else:    
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            return curr.word
        return dfs(self.root, 0)
            

        
                