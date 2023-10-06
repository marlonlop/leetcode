class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        # rob1, rob2, n, n+1, n+2, ...
        # rob1, rob2, 2,  7,   9,  3, 1
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

'''
time O(n) n=len(nums)
space O(1) 
'''