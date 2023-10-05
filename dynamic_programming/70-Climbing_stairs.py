class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        stairs    1     2    3        4     5
        # ways    1     2  2+1=3    2+3=5  3+5=8   #same as fibonacci sequence
        '''
        # base case
        if n <= 2:#
            return n 
        s1, s2 = 1, 1 #for memoization
        for n in range(1, n):
            current = s1 + s2 #temp to keep sum of s1, s2 before rewriting them
            s1 = s2
            s2 = current
        return s2

        '''
        # bottom up dp solution
        s1, s2 = 1, 1
        for i in range(n - 1):
            temp = s1
            s1 = s1 + s2
            s2 = temp
        return s1
        '''