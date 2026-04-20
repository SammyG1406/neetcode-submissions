class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maximum = 0
        m, n = len(grid), len(grid[0])

        def checkCell(r,c):
            if(min(r,c) < 0 or r == m or n == c or grid[r][c] == 0 or (r,c) in visited):
                return 0
            visited.add((r,c))
            count = 1
            count += checkCell(r + 1, c)
            count += checkCell(r -1, c)
            count += checkCell(r, c + 1)
            count += checkCell(r, c - 1)

            return count
        

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    maximum = max(maximum, checkCell(i, j))
        
        return maximum

        