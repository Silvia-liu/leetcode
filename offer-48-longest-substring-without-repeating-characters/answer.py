# 暴力解法 是on3，太慢了
# 方法一 动态规划+哈希表
"abcabcbb"
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1) # 获取索引 i  如果没有相同的值，那就返回默认值-1，如果有相同的值，那就是当前s[j]的左边最近的相同字母的索引，比如当前j=4(b)，则本行代码返回1(b)，
            dic[s[j]] = j # 更新哈希表，更新字母的最新索引
            tmp = tmp + 1 if tmp < j - i else j - i # dp[j - 1] -> dp[j]  # 动态规划方程
            res = max(res, tmp) # max(dp[j - 1], dp[j])  
        return res

动态规划解析：
状态定义： 设动态规划列表 dp ，dp[j] 代表以字符 s[j] 为结尾的 “最长不重复子字符串” 的长度。

转移方程： 固定右边界 j ，设字符 s[j] 左边距离最近的相同字符为 s[i] ，即 s[i] = s[j] 。

当 i<0 ，即 s[j] 左边无相同字符，则dp[j]=dp[j−1]+1 ；
当 dp[j−1]<j−i ，说明字符 s[i] 在子字符串 dp[j−1] 区间之外 ，则dp[j]=dp[j−1]+1 ；
当 dp[j−1]≥j−i ，说明字符 s[i]在子字符串 dp[j-1]区间之中 ，则 dp[j]的左边界由 s[i] 决定，即dp[j]=j−i ；
当 i < 0时，由于 dp[j−1]≤j 恒成立，因而 dp[j−1]<j−i 恒成立，因此分支 1. 和 2. 可被合并。
方程：dp[i] = dp[i-1] + 1 if dp[i-1] < j - i else j - i 

返回值：max(dp) ，即全局的 “最长不重复子字符串” 的长度。


