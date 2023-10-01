class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(idx, possibleComb, total):
            if total == target:
                res.append(possibleComb.copy())
                return
            if idx >= len(candidates) or total > target:
                return
            
            ### decision tree to include current candidates[i] ###
            possibleComb.append(candidates[idx])
            #not incressing idx bc it may contain dup current cadidate
            #also adding value of current candidate to total
            backtrack(idx, possibleComb, total + candidates[idx]) 

            ### decision tree NOT to include current candidates[i] ###
            possibleComb.pop() #removing current candidate that was added above
            #advancing idx to next cadidate, total remains unchanged cuz not inc curr candidate
            backtrack(idx + 1, possibleComb, total)

            return
        
        backtrack(0, [], 0)
        return res