class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        n = len(heights)

        for idx, height in enumerate(heights):
            area = 0
            start = idx
            while stack and stack[-1][1] > height:
                stackIdx, stackHeight = stack.pop()
                stackArea = (idx - stackIdx) * stackHeight
                maxArea = max(stackArea, maxArea)
                start = stackIdx
            stack.append([start, height])

        for idx, height in stack:
            maxArea = max(maxArea, height * (n - idx))
            
        return maxArea
