class MinStack:

    def __init__(self):
        self.stack = []
        self.num_counts = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val in self.num_counts:
            self.num_counts[val] += 1
        else:
            self.num_counts[val] = 1

    def pop(self) -> None:
        val = self.stack.pop()
        self.num_counts[val] -= 1
        if self.num_counts[val] == 0:
            del self.num_counts[val]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.num_counts.keys())
        