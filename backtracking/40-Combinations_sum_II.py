class Solution:
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(comb, index, target):
            if target  == 0:
                res.append(comb.copy())
                return
            if target <= 0:
                return
            
            prev = -1
            for i in range(index, len(candidates)):
                if candidates[i] == prev:
                    continue
                comb.append(candidates[i])
                backtrack(comb, i + 1, target - candidates[i])
                comb.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res

        '''
        time O(2^n)
        space O(n)
        '''