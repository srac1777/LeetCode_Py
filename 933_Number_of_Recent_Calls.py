from collections import deque


class RecentCounter:

    def __init__(self):
        self.rc = deque([])

    def ping(self, t: int) -> int:
        if t != None:
            self.rc.append(t)
            while self.rc[0] < t-3000:
                self.rc.popleft()
        return len(self.rc)
