class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visited = set()

        def dfs(r, c):
            if (r not in range(rows)
                or c not in range(cols)
                or (r, c) in visited
                or grid[r][c] == 0
            ):
                return 0

            visited.add((r, c))
            ''' 
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            curArea = 0
            for rowD, colD in directions:
                curArea += dfs(r + rowD, c + colD)
            return curArea + 1
            '''
            # concised return and more readable
            return (1 + dfs(r + 1, c)
                    + dfs(r - 1, c)
                    + dfs(r, c + 1)
                    + dfs(r, c - 1))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1   and (r, c) not in visited:
                    maxArea = max(maxArea, dfs(r, c))
                    
        return maxArea
        
'''
time O(m*n)
space O(m*n)
'''