class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        land = set()
        def checkSurrounding(r,c):
            if(min(r,c)<0 or r == m or c==n or grid[r][c]=="0" or (r,c) in land):
                return
            land.add((r,c))
            checkSurrounding(r, c+1)
            checkSurrounding(r, c-1)
            checkSurrounding(r-1, c)
            checkSurrounding(r+1, c)
    
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in land:
                    islands += 1
                    checkSurrounding(i, j)
        return islands