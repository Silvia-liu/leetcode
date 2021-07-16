# 反正我是不会的
# 不搬题解了，搬了也看不太懂，注意代码界面有一个python提交的，可以参考
class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [1.0 / 6.0] * 6
        for i in range(2, n + 1):
            tmp = [0] * (5 * i + 1)
            for j in range(len(dp)):
                for k in range(6):
                    tmp[j + k] += dp[j] / 6
            dp = tmp
        return dp

