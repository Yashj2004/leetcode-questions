class Solution:
    def minDays(self, grid: List[List[int]]) -> int:

        def island_count(grid):
            new_grid=[[0 for i in range(len(grid[0]))]for i in range(len(grid))]
            count=0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==1 and new_grid[i][j]==0:
                        dfs(grid,i,j,new_grid)
                        count+=1
            return count

        def dfs(grid,i,j,new_grid):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==0 or new_grid[i][j]==1:
                return
            new_grid[i][j]=1
            dfs(grid,i-1,j,new_grid)
            dfs(grid,i+1,j,new_grid)
            dfs(grid,i,j-1,new_grid)
            dfs(grid,i,j+1,new_grid)

        row=len(grid)
        col=len(grid[0])
        count=island_count(grid)

        if count!=1:
            return 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    grid[i][j]=0
                    c=island_count(grid)
                    if c!=1:
                        return 1
                    grid[i][j]=1
        return 2
            


