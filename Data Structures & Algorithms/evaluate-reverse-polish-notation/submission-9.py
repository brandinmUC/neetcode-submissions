class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                stack.append(stack.pop(-2) - stack.pop())
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                stack.append(int(stack.pop(-2) / stack.pop()))
            else:
                stack.append(int(c))
        return stack[0]
            