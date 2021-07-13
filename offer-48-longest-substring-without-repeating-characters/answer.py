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
# 方法二 哈希表+双指针
哈希表 dic统计： 指针 j 遍历字符 s ，哈希表统计字符 s[j] 最后一次出现的索引 。
更新左指针 i ： 根据上轮左指针 i 和 dic[s[j]] ，每轮更新左边界 i ，保证区间[i+1,j] 内无重复字符且最大。i=max(dic[s[j]],i)
更新结果 res ： 取上轮 res和本轮双指针区间 [i+1,j] 的宽度（即 j−i ）中的最大值。res=max(res,j−i)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, i = {}, 0, -1  # i 初始值为-1
        for j in range(len(s)):
            if s[j] in dic:  # 如果s[j]在dic中了，说明已经是第二次出现了，
                i = max(dic[s[j]], i) # 更新左指针 i 为最新出现的重复字符s[j]，的上一次出现时对应的索引
            dic[s[j]] = j # 哈希表记录，s[j]这个元素新的索引
            res = max(res, j - i) # 更新结果  如果新的j-i更大，那就是res = j-i
        return res



# 方法3：动态规划加线性遍历

左边界 i 获取方式： 遍历到 s[j] 时，初始化索引 i = j - 1，向左遍历搜索第一个满足 s[i]=s[j] 的字符即可   时间复杂度on2
"abcabcbb"
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         dic = {}

        res = tmp = i = 0
        for j in range(len(s)):
            i = j-1
            while i >= 0 and s[i] != s[j]: i -= 1 # 线性查找 i
#             i = dic.get(s[j], -1) # 获取索引 i  如果没有相同的值，那就返回默认值-1，如果有相同的值，那就是当前s[j]的左边最近的相同字母的索引，比如当前j=4(b)，则本行代码返回1(b)，
#             dic[s[j]] = j # 更新哈希表，更新字母的最新索引
            tmp = tmp + 1 if tmp < j - i else j - i # dp[j - 1] -> dp[j]  # 动态规划方程
            res = max(res, tmp) # max(dp[j - 1], dp[j])  
        return res


