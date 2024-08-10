class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        row=len(grid)
        col=len(grid[0])
        new_grid=[[0 for i in range(col*3)]for i in range(row*3)]
        for i in range(row):
            for j in range(col):
                r=i*3
                c=j*3
                if grid[i][j]=='\\':
                    new_grid[r][c]=1
                    new_grid[r+1][c+1]=1
                    new_grid[r+2][c+2]=1
                elif grid[i][j]=='/':
                    new_grid[r][c+2]=1
                    new_grid[r+1][c+1]=1
                    new_grid[r+2][c]=1
        def fill(new_grid,i,j):
            if i<0 or i>=len(new_grid) or j<0 or j>=len(new_grid[0]) or new_grid[i][j]!=0:
                return
            new_grid[i][j]=1
            fill(new_grid,i-1,j)
            fill(new_grid,i,j+1)
            fill(new_grid,i+1,j)
            fill(new_grid,i,j-1)
        count=0
        for i in range(len(new_grid)):
            for j in range(len(new_grid[0])):
                if new_grid[i][j]==0:
                    fill(new_grid,i,j)
                    count+=1
        return count
