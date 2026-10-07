class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]
        stack = [(len(temperatures) - 1, temperatures[-1])]
        
        for i in range(len(temperatures) - 2, -1, -1):
            temp = temperatures[i]
            found = False
            while stack != []:
                if temp >= stack[-1][1]:
                    stack.pop()
                else:
                    result.append(stack[-1][0] - i)
                    stack.append((i, temp))
                    found = True
                    break
            if not found:
                result.append(0)
                stack.append((i, temp))
            # if temp > stack -> pop until empty -> 0 else: append dist to result -> add temp to stack

        return result[::-1]
