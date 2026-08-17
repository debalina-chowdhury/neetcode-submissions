from collections import deque
class ZigzagIterator:

    def __init__(self, v1: List[int], v2: List[int], fill_value=None):
        self.q = deque([(v,0) for v in (v1, v2) if v])

    def next(self) -> int:
        v, i = self.q.popleft()
        if i + 1 < len(v):
            self.q.append((v, i + 1))
        return v[i]


    def hasNext(self) -> bool:
        return len(self.q) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
