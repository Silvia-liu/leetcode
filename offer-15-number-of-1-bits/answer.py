class Solution:
    def hammingWeight(self, n: int) -> int:
        # 方法一
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res
        # 方法二
        
        # 方法三
