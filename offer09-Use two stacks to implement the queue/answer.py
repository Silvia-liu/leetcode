class CQueue:

    def __init__(self):
        self.A = []
        self.B = []
        #
            


    def appendTail(self, value: int) -> None:
        
        self.A.append(value)
        


    def deleteHead(self) -> int:
        if self.B:return self.B.pop()  # self.B里面有数字
        if not self.A:return -1  # 如果self.B里没数字，看self.A里面有无，无则 -1
        while self.A:  # 如果self.A里面有数字，且appendTail函数调用多次，self.A不止一个数，所以一个while，全部放到self.B里面，并且最后pop（）出最开始的一个元素
            self.B.append(self.A.pop())
        return self.B.pop()
        
        
# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
