class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, stackIdx = stack.pop()
                result[stackIdx] = i - stackIdx
            stack.append((temp,  i))
        return result
