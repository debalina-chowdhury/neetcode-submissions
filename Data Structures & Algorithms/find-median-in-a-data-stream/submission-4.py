import heapq
class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:        
        self.heap.append(num)
        self.heap.sort()

    def findMedian(self) -> float:
        if len(self.heap) == 0:
            return -1
        if len(self.heap) % 2 == 0:
            mid = (len(self.heap) // 2) - 1
            mid_next = len(self.heap) // 2
            return (self.heap[mid] + self.heap[mid_next])/2
        else:
            mid = len(self.heap) // 2
            return float(self.heap[mid])