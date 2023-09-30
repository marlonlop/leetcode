class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True

    def search(self, word: str) -> bool:
        
        def dfs(ind, root):
            cur = root
            for i in range(ind, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                elif c not in cur.children:
                    return False
                else:
                    cur = cur.children[c]
            return cur.isWord
        
        return dfs(0, self.root)