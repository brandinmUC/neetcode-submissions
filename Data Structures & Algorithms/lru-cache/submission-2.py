class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.table = {} # key, val (Node) pairs
        self.capacity = capacity

        # Left - LRU, Right - MRU        
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int: # does get make it mru? - yes
        if key in self.table:
            self.remove(self.table[key])
            self.insert(self.table[key])
            return self.table[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.table:
             self.remove(self.table[key])
        self.table[key] = ListNode(key, value)
        self.insert(self.table[key])

        if len(self.table) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.table[lru.key]