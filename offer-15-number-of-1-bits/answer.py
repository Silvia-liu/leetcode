class Solution:
    def hammingWeight(self, n: int) -> int:
        # 方法一 最常用的方法
        res = 0
        while n:
            res += n & 1
            n >>= 1  # 逐位左移
        return res
    # 方法二  巧用n&(n-1)  &=是按位处理
#     def hammingWeight(self, n: int) -> int:
#     res = 0
#     while n:
#         res += 1
#         n &= n - 1
#     return res
     
