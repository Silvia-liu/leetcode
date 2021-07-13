# 暴力解法
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tem = '' # 遍历过程中的字符串
        res = 0  #最终返回值
        temp_res = 0  # 暂存字串长度
        for i in s:
            if i in tem:
                temp_res = len(tem)
                tem = i
                if res<=temp_res:
                    res = temp_res
            else:
                tem += i
        if len(tem) >= res:  # 都不重复
            res = len(tem)
        return res
                

