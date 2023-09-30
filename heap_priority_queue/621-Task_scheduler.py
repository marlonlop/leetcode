class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = Counter(tasks) # dict with counts of tasks
        maxHeap = [ -cnt for cnt in counts.values()]
        heapq.heapify(maxHeap)
        
        q = deque() # pairs of [-count, iddle time]
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap) # negative cnt in maxHeap
                if count: # if cnt != 0
                    q.append([count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
        