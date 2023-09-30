class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)

        while k > 1:
            n = -(heapq.heappop(nums))
            k -= 1
        return -nums[0]