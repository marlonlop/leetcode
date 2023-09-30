class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        keysMinHeap = []
        for point in points:
            x, y = point
            sq = (x - 0)**2 + (y - 0)**2 
            keysMinHeap.append([sq, x, y])
        
        heapq.heapify(keysMinHeap)
 
        res = []
        i = 0
        while i < k:
            print(i)
            _, x, y = heapq.heappop(keysMinHeap)
            res.append([x, y])
            i += 1
        return res
        