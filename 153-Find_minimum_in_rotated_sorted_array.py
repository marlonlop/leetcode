class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        res = 5000

        if len(nums) == 1:
            return nums[0]

        while l != r:
            m = (l + r) // 2
            res = min(res, nums[m], nums[l], nums[r])
            print(res)
            if nums[m] > nums[l] :
                l = m
            else: # m < l:
                r = m

        return res