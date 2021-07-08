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
算法流程：
初始化： 声明 i, j 双指针分别指向 nums 数组左右两端；
循环二分： 设 m = (i + j) / 2 为每次二分的中点（ "/" 代表向下取整除法，因此恒有i≤m<j ），旋转点x，就是要返回的点，就是右边排序数组的最小值。可分为以下三种情况：
当 nums[m] > nums[j] 时： m 一定在 靠左边那个有序数组 中，即旋转点 x 一定在 [m + 1, j] 闭区间内，因此执行 i = m + 1,将旋转点x缩小范围至m右边；
当 nums[m] < nums[j] 时： m 一定在 右排序数组 中，即旋转点 x 一定在[i, m] 闭区间内，因此执行 j = m，将旋转点x缩小范围至m左边；
当 nums[m] = nums[j] 时： 无法判断 m 在哪个排序数组中，即无法判断旋转点 x 在 [i, m] 还是 [m + 1, j] 区间中。解决方案： 执行 j = j - 1 缩小判断范围，分析见下文。
当出现 nums[m] = nums[j] 时，一定有区间 [i, m] 内所有元素相等 或 区间 [m, j] 内所有元素相等（或两者皆满足）。
对于寻找此类数组的最小值问题，可直接放弃二分查找，而使用线性查找替代。即方法二 



返回值： 当 i = j 时跳出二分循环，并返回 旋转点的值 nums[i] 即可。

 class Solution:
    def minArray(self, numbers: [int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]: i = m + 1
            elif numbers[m] < numbers[j]: j = m
            else: j -= 1  # 方法一
            else: return min(numbers[i:j])  # 方法二
        return numbers[i]

