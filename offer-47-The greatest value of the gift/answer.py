设 f(i, j)f(i,j) 为从棋盘左上角走至单元格 (i ,j)的礼物最大累计价值，易得到以下递推关系：f(i,j) 等于 f(i,j-1) 和 f(i-1,j)中的较大值加上当前单元格礼物价值 grid(i,j)。
f(i,j)=max[f(i,j−1),f(i−1,j)]+grid(i,j)
因此，可用动态规划解决此问题，以上公式便为转移方程。

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(1, n): # 初始化第一行，注：range(1, n)最大值为n-1
            grid[0][i]+=grid[0][i-1]
        for i in range(1, m): # 初始化第一列
            grid[i][0]+=grid[i-1][0]
        for i in range(1, m):
            for j in range(1,n):
                grid[i][j] += max(grid[i][j-1], grid[i-1][j])  # 自身的值加上左边或右边来的值,才是当前的最大值
        return grid[-1][-1]

