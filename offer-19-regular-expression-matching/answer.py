class Solution:
    # "."表示任意一个字符
    # "*"表示前面的字符可以出现任意次，包括0次（清除前面字符）
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        # 初始化全部dp 为False
        dp = [[False] * n for _ in range(m)]
        # dp[0][0]为真，说明两个空字符串可以匹配
        dp[0][0] = True
        # 首行 s 为空字符串，因此当 p 的偶数位为 * 时才能够匹配（即，可以让 p 的奇数位出现 0 次，保持 p 是空字符串）。因此，循环遍历字符串 p ，步长为 2（即只看偶数位）。
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'        
        # 让一个S去适配全部p里面的字符串，然后逐个匹配S各个字符
        # 对S遍历
        for i in range(1, m):
            # 对 p遍历
            for j in range(1, n):
                # 如果if p[j - 1] == '*'，则dp[i][j] = dp[i][j - 2] or dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.')
                # 否则 dp[i - 1][j - 1] and (p[j - 1] == '.' or s[i - 1] == p[j - 1])  左侧表达式为真，则dp[i][j]=1（True）
                dp[i][j] = dp[i][j - 2] or dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.') \
                           if p[j - 1] == '*' else \
                           dp[i - 1][j - 1] and (p[j - 1] == '.' or s[i - 1] == p[j - 1])
        return dp[-1][-1]
    
    # 这道题值得再多看几次
