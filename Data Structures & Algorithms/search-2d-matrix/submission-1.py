class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] >= target:
                if row[-1] == target:
                    return True
                return self.binarySearch(row, target)
        return False
        
    def binarySearch(self, lst, target):
        l = 0
        r = len(lst) - 1
        while l <= r:
            mid = ((r - l) // 2) + l
            if lst[mid] == target:
                return True
            elif lst[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
