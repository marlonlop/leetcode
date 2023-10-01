class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for c in range(n)]
        cols = set()
        upDiag = set() # (r + c)
        downDiag = set() # (r - c)

        def backtrack(r):
            if r == n:
                tmp = ["".join(row) for row in board]
                result.append(tmp)
                return
            
            for c in range(n):
                if (c in cols 
                    or (r + c) in upDiag
                    or (r - c) in downDiag):
                    continue
                
                # adding c and diag and "Q" values to explore possible tree solution
                cols.add(c)
                upDiag.add(r + c)
                downDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                # removing c and diag values from sets to backtrack to prev row and try next col position
                # bc tree in this path did not yield a valid solution
                cols.remove(c)
                upDiag.remove(r + c)
                downDiag.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return result