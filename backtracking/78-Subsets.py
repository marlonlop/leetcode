class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerSet = []
        subset = []

        def backtrack(idx):
            if idx >= len(nums):
                #powerSet.append(subset.copy())
                powerSet.append(subset[:]) #more efficient 
                return
            
            # decision tree to include current nums[idx]
            subset.append(nums[idx])
            backtrack(idx + 1)

            # decision tree NOT to include current nums[idx]
            subset.pop() # removing current nums[idx] that was added in line 12
            backtrack(idx + 1)
        
        backtrack(0)
        return powerSet

'''
time O(n * 2^n)
space O(n)                                  *
                            [1]                               []
                [1,2]               [1]               [2]             []
         [1,2,3]     [1,2]     [1,3]    [1]      [2,3]   [2]      [3]    []  
'''