class Node:
    def __init__(self, children, isWord):
        self.children = children
        self.isWord = isWord
class Autocomplete:
    def build(self, words):
        self.trie = Node(False, {})
        for word in words:
            current = self.trie
            for char in word:
                if not char in current.children:
                    current.children[char] = Node({}, False)
                current = current.children[char]
            current.isWord = True
    def autocomplete(self, prefix):
        current = self.trie
        for char in word:
            if not char in current.children:
                return []
            current = current.children[char]
            return self._findwordFromNode(current, word)
    def _findwordFromNode(self, node, prefix):
        words = []
        if node.isWord:
            words.append(prefix)
        for char in node.children:
            words += self._findwordFromNode(node, node.children[char], prefix + char)
        return words
if __name__ == "__main__":
    s = Autocomplete()
    s.build(["beam", "brick", "been", "bunker", "tip", "brink", "beak"])
    print(s.autocomplete('be'))
