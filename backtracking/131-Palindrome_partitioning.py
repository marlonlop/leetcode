class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalin(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        res = []
        part = []
        def backtrack(idx):
            if idx >= len(s):
                res.append(part[:])
                return
            
            for rIdx in range(idx, len(s)):
                if isPalin(s, idx, rIdx):
                    part.append(s[idx:rIdx + 1])
                    backtrack(rIdx + 1)
                    part.pop()
        backtrack(0)
        return res