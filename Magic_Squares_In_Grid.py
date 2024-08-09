class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0]) 
        def row_check(i,j,grid):
            r1= grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]
            r2= grid[i][j-1] + grid[i][j] + grid[i][j+1]
            r3= grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
            if r1!=15 or r2!=15 or r3!=15:
                return False
            return True

        def col_check(i,j,grid):
            c1= grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j-1]
            c2= grid[i-1][j] + grid[i][j] + grid[i+1][j]
            c3= grid[i-1][j+1] + grid[i][j+1] + grid[i+1][j+1]
            if c1!=15 or c2!=15 or c3!=15:
                return False
            return True

        def dia_check(i,j,grid):
            d1= grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1]
            d2= grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1]
            if d1!=15 or d2!=15:
                return False
            return True
        
        def check_uniq(i,j,grid):
            uni=[0]*10
            for m in range(i-1, i+2):
                for n in range(j-1,j+2):
                    if grid[m][n]<=9:
                        uni[grid[m][n]]+=1
                    else:
                        return False
            for a in range(len(uni)):
                if uni[a]>1:
                    return False
            return True 


        if row<3 and col<3:
            return 0
        ans=0
        for i in range(1,row-1):
            for j in range(1,col-1):
                if check_uniq(i,j,grid) and  row_check(i,j,grid) and  col_check(i,j,grid) and dia_check(i,j,grid):
                    ans+=1
                    print(i,j)
        return ans
