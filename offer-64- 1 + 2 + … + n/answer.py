class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)  # 这一句真的绝，判断n = 0的时候退出函数，在self.sumNums()在函数体内执行逐个-1操作
        self.res += n
        return self.res
