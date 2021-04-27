class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []
        self.B = []


    def push(self, x: int) -> None:
        self.A.append(x)
        if len(self.B) == 0 or self.B[-1] >= x:
            self.B.append(x)


    def pop(self) -> None: 
      #1
        # if self.B[-1] == self.A.pop():
            # self.B.pop()
      #2
        if self.B[-1] == self.A[-1]:
            self.B = self.B[:-1]
        self.A = self.A[:-1]
        


    def top(self) -> int:
        return self.A[-1]


    def min(self) -> int:
        return self.B[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
