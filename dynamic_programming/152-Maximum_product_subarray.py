class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = max(nums)
        curMin, curMax = 1, 1
        
        for n in nums:
            # if statement not needed
            # if n == 0:
            #     curMin, curMax = 1, 1
            #     continue
            
            temp = curMax * n
            # if above not needed bc
            # curMax=2 and n=0, curMin=-1, then line 16= 0
            # in next iter curMax will be equal to whatever value n is
            curMax = max(n * curMax, n * curMin, n) # curMax= max(2*0, 0*-1, 0 ) = 0
            curMin = min(temp, n * curMin, n)
            output = max(output, curMax)
        return output