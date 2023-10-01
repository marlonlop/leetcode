class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitsMap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"}

        def backtrack(idx, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitsMap[digits[idx]]:
                backtrack(idx + 1, curStr + c)
        
        if digits:
            backtrack(0, "")
        return res

'''
time O(n*4^n) # 4 comes from digits 7,9 which have 4 chars each
space O(n)  n=len(digits)
'''