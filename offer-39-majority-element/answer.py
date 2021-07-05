本题常见的三种解法：

哈希表统计法： 遍历数组 nums ，用 HashMap 统计各数字的数量，即可找出 众数 。此方法时间和空间复杂度均为 O(N) 。
数组排序法： 将数组 nums 排序，数组中点的元素 一定为众数。
摩尔投票法： 核心理念为 票数正负抵消 。此方法时间和空间复杂度分别为 O(N) 和 O(1) ，为本题的最佳解法。
摩尔投票法：
设输入数组 nums 的众数为 xx ，数组长度为 nn 。

推论一： 若记 众数 的票数为 +1 ，非众数 的票数为 -1 ，则一定有所有数字的 票数和 > 0 。

推论二： 若数组的前 a个数字的 票数和 = 0 ，则 数组剩余 (n-a)个数字的 票数和一定仍 >0，即后 (n-a)个数字的 众数仍为 x 


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote, count = 0, 0
        for num in nums:
            if vote == 0:x = num
            vote += 1 if x == num else -1
        # 验证这个时候的vote是不是众数（超过一半）
        for num in nums:
            if x == num:
                count+=1
        return x if count>=len(nums)/2 else 0  # 无众数的时候返回0
