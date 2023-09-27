class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = 0 # will reuse fast pointer as a slow in next loop
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


        """
        # Time O(n) and Space O(1)
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: 
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        """
        '''
        # Time O(n) and Space O(n)
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)
        '''