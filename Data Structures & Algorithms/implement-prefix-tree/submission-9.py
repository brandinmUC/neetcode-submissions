class PrefixTree:

    def __init__(self):
        self.tries = {}

    def insert(self, word: str) -> None:
        if word[0] not in self.tries:
            self.tries[word[0]] = Trie()

        self.tries[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        if word[0] not in self.tries:
            return False

        return self.tries[word[0]].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if prefix[0] not in self.tries:
            return False

        return self.tries[prefix[0]].startsWith(prefix[1:])


class Trie:

    def __init__(self):
        self.children = {}
        self.final = False

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.final = True
            return

        if word[0] not in self.children:
            self.children[word[0]] = Trie()

        self.children[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.final

        if word[0] not in self.children:
            return False

        return self.children[word[0]].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True

        if prefix[0] not in self.children:
            return False

        return self.children[prefix[0]].startsWith(prefix[1:])