class MedianFinder:

    def __init__(self):
        self.smallHeap, self.largeHeap = [], []

    def addNum(self, num: int) -> None:
            heapq.heappush(self.smallHeap, -num)

            # tp maintain onle smallest values in smallHeap
            if (self.smallHeap and self.largeHeap and 
                -(self.smallHeap[0]) > self.largeHeap[0]):
                val = -(heapq.heappop(self.smallHeap))
                heapq.heappush(self.largeHeap, val)
            
            # to maintain lenght of both heaps is not > 2
            if (len(self.smallHeap) > len(self.largeHeap) + 1):
                val = -(heapq.heappop(self.smallHeap))
                heapq.heappush(self.largeHeap, val) 
            if (len(self.largeHeap) > len(self.smallHeap) + 1):
                val = heapq.heappop(self.largeHeap)
                heapq.heappush(self.smallHeap, -val)

    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.largeHeap):
            return -self.smallHeap[0]
        elif len(self.largeHeap) > len(self.smallHeap):
            return self.largeHeap[0]
        else:
            return (-self.smallHeap[0] + self.largeHeap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# 2,5,1,6,3,8,4,3,9,0