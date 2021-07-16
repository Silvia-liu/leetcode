# 拿到题目以后，是有点懵，但是，看了题解就瞬间明朗

# 其实就是有规律的去延伸后面的第n个符合条件的数
# 这个“规律”就是动态规划方程
# 同时注意初始化，边界条件，和返回值，即可

动态规划解析：
状态定义： 设动态规划列表 dpdp ，dp[i]dp[i] 代表第 i + 1i+1 个丑数；
转移方程：
当索引 a, b, ca,b,c 满足以下条件时， dp[i]为三种情况的最小值；
每轮计算 dp[i]dp[i] 后，需要更新索引 a, b, c 的值，使其始终满足方程条件。实现方法：分别独立判断
dp[a]×2>dp[i−1]≥dp[a−1]×2
dp[b]×3>dp[i−1]≥dp[b−1]×3
dp[c]×5>dp[i−1]≥dp[c−1]×5

dp[i]=min(dp[a]×2,dp[b]×3,dp[c]×5)

初始状态： dp[0] = 1，即第一个丑数为 1 ；
返回值： dp[n-1]，即返回第 n个丑数；

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5  # 这个就是规律
            dp[i] = min(n2, n3, n5)  # 取最小的丑数
            if dp[i] == n2: a += 1  # 是他 是他 就是他，然后推出下一个丑数，并且自己+1
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]

