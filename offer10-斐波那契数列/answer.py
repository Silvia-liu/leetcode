class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        # sum_tmp = 0
        for i in range(n):
            a, b = b, (a + b) % 1000000007
            # a = b
            # b = sum_tmp
        return a
