# encoding: utf-8


class Solution:
    def DFS(self,tmp,row,col,area):
        tmp[row][col]=2
        area+=1
        if row-1>=0 and 1==tmp[row-1][col]:
            area=self.DFS(tmp,row-1,col,area)
        if row+1<=len(tmp)-1 and 1==tmp[row+1][col]:
            area=self.DFS(tmp,row+1,col,area)
        if col-1>=0 and 1==tmp[row][col-1]:
            area=self.DFS(tmp,row,col-1,area)
        if col+1<=len(tmp[0])-1 and 1==tmp[row][col+1]:
            area=self.DFS(tmp,row,col+1,area)
        return area
    def maxAreaOfIsland(self, grid):
        if []==grid or [[]]==grid:
            return 0
        m=len(grid)
        n=len(grid[0])
        res=0
        area=0
        for i in range(m):
            for j in range(n):
                if 1==grid[i][j]:
                    area=self.DFS(grid,i,j,area)
                    res=max(res,area)
                    area=0
        return res

if __name__ == '__main__':
    arr = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    solution = Solution()

    print('A中最大连续取1值的区域中1的个数为：',solution.maxAreaOfIsland(arr))


