class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def maxRob(houses):
            rob1, rob2 = 0, 0
            for h in houses:
                # rob1, rob2, 1,2,3,1
                temp = max(rob1 + h, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
        
        return max(maxRob(nums[:-1]), maxRob(nums[1:]))

'''
time O(n) n=len(nums)
space O(1)
'''