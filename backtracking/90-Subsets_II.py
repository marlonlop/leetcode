class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        powerSet = []
        nums.sort()

        def backtrack(idx, subset):
            if idx >= len(nums):
                powerSet.append(subset[:])
                return

            # tree to include current nums[idx]
            subset.append(nums[idx])
            backtrack(idx + 1, subset)

            # tree not to include current nums[idx]
            subset.pop()
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            backtrack(idx + 1, subset) # 

        backtrack(0, [])
        return powerSet

    '''
    time O(n*2^n)
    space O(2^n)
    '''