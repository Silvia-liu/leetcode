class Solution:
    def strToInt(self, str: str) -> int:
        res, i, sign, length = 0, 0, 1, len(str)  # 初始化变量
        int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10  # int_max = 2147483647   bndry = 214748364  各位少了一个7
        if not str: return 0         # 空字符串，提前返回
        while str[i] == ' ':  # 去除空格
            i += 1
            if i == length: return 0 # 字符串全为空格，提前返回
        if str[i] == '-': sign = -1  # 记录负号
        if str[i] in '+-': i += 1  # 不论当前的符号是+还是-，都是只有一位，然后向后读取一位（i+=1）
        for j in range(i, length):
            if not '0' <= str[j] <= '9' : break  # 碰到非数字的就直接break，一种是前有数字后有字母，则返回已读到的数字；另一种是一开始就碰到字母，则返回res初始值0
            if res > bndry or res == bndry and str[j] > '7':  # 前9位已经大于最大值中的前9位，后面在加什么都是超出范围，，同理，即使前9位和最大值的前9位一样，最后一位大于7，也是超出范围
                return int_max if sign == 1 else int_min  # 即使是数字部分超过最大值了，也要判断一下符号，选择返回最大值还是最小值
            res = 10 * res + ord(str[j]) - ord('0')  # *10是因为，没往后读一位，原本的数就乘了10，比如，423，读到42时是42，准备读下一位时，42变420，再加上第三位的3，组成423
        return sign * res  # 最后返回带有符号的结果
