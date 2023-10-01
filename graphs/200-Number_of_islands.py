class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0 
        visited = set()

        def dfs(r, c):
            if (r not in range(rows)
                or c not in range(cols)
                or (r, c) in visited
                or grid[r][c] == "0"

            ):
                return
            # try all directions for recursive dfs
            directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
            visited.add((r, c)) # add current coordinate to visited set, to check in other recur calls base case
            for drow ,dcol in directions:
                dfs(r + drow, c + dcol)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        return islands
'''
time O(m*n)
space O(m*n)
'''