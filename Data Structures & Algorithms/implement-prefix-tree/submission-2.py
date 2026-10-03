class PrefixTree:

    def __init__(self):
        self.tries = {}

    def insert(self, word: str) -> None:
        if word[0] not in self.tries:
            self.tries[word[0]] = Trie(word[0])
        self.tries[word[0]].insert(word)

    def search(self, word: str) -> bool:
        return self.tries[word[0]].search(word)

    def startsWith(self, prefix: str) -> bool:
        return False if (prefix[0] not in self.tries) else self.tries[prefix[0]].startsWith(prefix)


class Trie:

    def __init__(self, root):
        self.root = root
        self.children = {}
        self.final = False

    def insert(self, word: str) -> None:
        first, *rest = word
        if len(word) == 0 or first != self.root:
            return

        if len(word) == 1:
            self.final = True
            return
        
        if rest[0] not in self.children:
            self.children[rest[0]] = Trie(rest[0])

        self.children[rest[0]].insert(rest)

    def search(self, word: str, isprefix=False) -> bool:
        first, *rest = word

        if len(word) == 0 or first != self.root:
            return False

        if len(word) == 1:
            return True if (self.final or isprefix) else False

        if rest[0] not in self.children:
            return False

        return self.children[rest[0]].search(rest, isprefix)

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, True)
        