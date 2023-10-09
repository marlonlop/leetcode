class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def maxRob(houses):
            rob1, rob2 = 0, 0
            for h in houses:
                #             h h+1 h+2 ...
                # rob1, rob2, 1, 2,  3,  1
                temp = max(rob1 + h, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
        
        return max(maxRob(nums[:-1]), maxRob(nums[1:]))
        # return max(nums[0], maxRob(nums[:-1]), maxRob(nums[1:]))
        # by adding nums[0] we could remove the if statement at begining of def rob()

'''
time O(n) n=len(nums)
space O(1)
'''