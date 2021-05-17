class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # 方法一
        #  return s[n:] + s[:n]        
        # 方法二
         res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return ''.join(res)
        # 方法三
        # res = ""
        # for i in range(n, len(s)):
        #     res += s[i]
        # for i in range(n):
        #     res += s[i]
        # return res
