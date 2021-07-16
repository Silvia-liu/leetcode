# 拿到题目以后，是有点懵，但是，看了题解就瞬间明朗

# 其实就是有规律的去延伸后面的第n个符合条件的数
# 这个“规律”就是动态规划方程
# 同时注意初始化，边界条件，和返回值，即可

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: a += 1
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]

