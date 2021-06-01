# 如果是数组 numsnums 有 一个 只出现一次的数字，因此无法通过异或直接得到这两个数字
# 异或运算有个重要的性质，两个相同数字异或为 00 ，即对于任意整数 aa 有 a \oplus a = 0a⊕a=0 。因此，若将 numsnums 中所有数字执行异或运算，留下的结果则为 出现一次的数字 xx 

# def singleNumber(self, nums: List[int]) -> List[int]:
#     x = 0
#     for num in nums:  # 1. 遍历 nums 执行异或运算
#         x ^= num      
#     return x;         # 2. 返回出现一次的数字 x 即可


# 本题难点： 数组 numsnums 有 两个 只出现一次的数字，因此无法通过异或直接得到这两个数字。
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:# 加入nums = [3,3,4,4,1,6]
        x, y, n, m = 0, 0, 0, 1
        for num in nums:         # 1. 遍历异或  n中放的是（1异或6）
            n ^= num
        while n & m == 0:        # 2. 循环左移，计算 m  # m 循环左移一位，直到 n & m ！= 0   这个m是一个标志位，记录着1和6的二进制的哪一位不同，
            m <<= 1       
        for num in nums:         # 3. 遍历 nums 分组   若 num & m != 0 , 划分至子数组 1 ，执行遍历异或
            if num & m: x ^= num # 4. 当 num & m != 0
            else: y ^= num       # 4. 当 num & m == 0
        return x, y              # 5. 返回出现一次的数字
