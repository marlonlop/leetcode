class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        
        for i in range(len(s)):
            for l, r in ((i,i), (i, i + 1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
            
        return count

        ''' 
        with helper func
        
        count = 0
        for i in range(len(s)):
            l = r = i
            count += self.countP(s, l, r)

            l, r = i, i +1
            count += self.countP(s, l, r)
        return count

    def countP(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
        '''

        """
        time O(n^2)
        space O(1) 
        """