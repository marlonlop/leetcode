class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        time, freshO = 0, 0
        q = deque()
        # go through grid, push rotten O to q and count fresh O
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    freshO += 1
        
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and freshO > 0:
            qLen = len(q)
            for rot in range(qLen):
                r, c = q.popleft()
                for rd, cd in dirs:
                    row, col = r + rd, c + cd
                    #check bounds and fresh, then make rotten
                    if (row not in range(rows)
                        or col not in range(cols)
                        or grid[row][col] != 1):
                        continue
                    
                    grid[row][col] = 2
                    q.append([row, col])
                    freshO -= 1
            time += 1
        
        return time if freshO == 0 else -1

'''
time O(m*n)
space O(m*n) worst case q could be size of grid m*n
'''