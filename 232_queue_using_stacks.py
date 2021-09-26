from collections import deque


class MyQueue:

    def __init__(self):
        self.s1 = deque([])
        self.s2 = deque([])

    def push(self, x: int) -> None:
        self.s1.appendleft(x)

    def pop(self) -> int:
        while len(self.s1) > 0:
            x = self.s1.popleft()
            self.s2.appendleft(x)
        m = self.s2.popleft()
        while len(self.s2) > 0:
            x = self.s2.popleft()
            self.s1.appendleft(x)
        return m

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return len(self.s1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
