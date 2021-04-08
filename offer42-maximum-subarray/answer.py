class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_now = 0
        sum_max = 0
        # 只有一个数的情况
        if len(nums) == 1 or max(nums) <= 0:
            return max(nums)
            # return nums[0] 
        # 全为负数的情况
        # if max(nums) <= 0:             
            # return max(nums)
        # 有负有正的情况
        for i in range(len(nums)):            
            sum_now += nums[i]
            if sum_now <= 0:
                sum_now = 0
            else:
                if sum_now > sum_max:
                    sum_max = sum_now                
        return sum_max
