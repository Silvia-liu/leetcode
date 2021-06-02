import queue
class MaxQueue:
       # 因题干要求时间复杂度，所以用空间换时间，
    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1  # 队列为空返回-1

    def push_back(self, value: int) -> None:
        self.queue.put(value)  # value的加入
        while self.deque and self.deque[-1] < value:
            self.deque.pop()  # value的加入让deque不再严格单调递减，所以删除最后一个，让value加入deque尾部
        self.deque.append(value)

    def pop_front(self) -> int:
        if self.queue.empty(): return -1  # 队列为空返回-1
        val = self.queue.get()  # 拿到queue的最头部的值
        if val == self.deque[0]:  # 如果这个值，是当前的最大值，所以，辅助队列deque也要删除左侧头部最大值、保证deque的头部永远是最大值
            self.deque.popleft()
        return val



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
