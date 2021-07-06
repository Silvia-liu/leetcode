# 这个经常考
动态规划解析：
状态定义： 设动态规划列表 dp ，dp[i] 代表以 prices[i] 为结尾的子数组的最大利润（以下简称为 前 ii 日的最大利润 ）。
转移方程： 由于题目限定 “买卖该股票一次” ，因此前 i 日最大利润 dp[i]等于前 i - 1 日最大利润 dp[i-1]和第 i日卖出的最大利润中的最大值。
     dp[i]=max(dp[i−1],prices[i]−min(prices[0:i]))↑
     前i日最大利润=max(前(i−1)日最大利润,第i日价格−前i日最低价格)
初始状态： dp[0] = 0dp[0]=0 ，即首日利润为 00 ；
返回值： dp[n - 1]dp[n−1] ，其中 nn 为 dpdp 列表长度。

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 这种是官网解法，内存和速度只打败了20 30%
        # cost, profit = float('+inf'), 0
        # for price in prices:
        #     cost = min(cost, price)
        #     profit = max(profit, price-min(cost, price))
        # return profit
        # 下面这个是同一个意思，但是打败了60 70%--------不靠谱分析，是频繁使用MIN MAX浪费了时间和内存
        res = 0
        if prices:
            mi = prices[0]
        for i in prices:
            if mi > i:
                mi = i 
            res = max(res,i-mi)
        return res
