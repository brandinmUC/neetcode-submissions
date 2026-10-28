class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []        

        def pickAndSum(idx, combo, total):
            if total == target:
                res.append(combo.copy())
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i] > target:
                    break

                combo.append(candidates[i])
                pickAndSum(i + 1, combo, total + candidates[i])
                combo.pop()

        pickAndSum(0, [], 0)
        return res 
