# 纪念第一次自己ac一道题，速度96%，时间38%--虽然是暴力解法
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        i, res = 0, 0
        for i in range(1, len(numbers)):
            if numbers[i] < numbers[i-1]:
                res = numbers[i]
                return res
        if i == len(numbers)-1:
            return numbers[0]
            
 # 官方解法
 class Solution:
    def minArray(self, numbers: [int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]: i = m + 1
            elif numbers[m] < numbers[j]: j = m
            else: j -= 1
        return numbers[i]

