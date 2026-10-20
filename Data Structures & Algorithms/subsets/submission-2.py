class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            cpy = res.copy()
            for subset in cpy:
                res += [subset + [num]]
        
        return res
        