class Solution:
    def translateNum(self, num: int) -> int:
        # 初始化
        s = str(num)
        a = b = 1  # 空字符串和单个数字，都只有一种翻译方式，所以 a b 都为1。a b就是记录翻译方式总数的
        for i in range(2, len(s) + 1): # 从第二个数字开始计算翻译方式总数，因为计算总的翻译方式是dp[i] = dp[i-1] + dp[i-2]所以i的最大值是len(s) + 1
            tmp = s[i - 2:i]  # 当前已经
            c = a + b if "10" <= tmp <= "25" else a  # 核心，如果两个字符的tmp只有一种翻译方式，那c = a 即 dp[i] = dp[i-1];如果有两种方式，那就是c = a + b 即  dp[i] = dp[i-1] + dp[i-2]
            b = a  # 逐个字符交替前进
            a = c
        return a 
