class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        
        # dfs func to capture unsurrounded regions (reverse thinking)
        def reverseCapture(r, c):
            if (r not in range(ROWS)
                or c not in range(COLS)
                or board[r][c] != "O"): # must != "O" to avoid edge case of all board being X
                return

            board[r][c] = "-"
            reverseCapture(r + 1, c)
            reverseCapture(r - 1, c)
            reverseCapture(r, c + 1)
            reverseCapture(r, c - 1)
        
        # capture all unsurrounded regions (only remaining Os)
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and 
                    (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    reverseCapture(r, c)

        # capture all surrounded regions (only remaining Os)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # flip all "-" back to "O"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "-":
                    board[r][c] = "O"

'''
time O(m*n)
space O(m*n)
'''