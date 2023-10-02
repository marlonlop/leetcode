from collections import deque
class Solution:
    def wallsAndGates(rooms):
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        def addRoom(r, c):
            if (r in range(ROWS)
                or c in range(COLS)
                or (r, c) in visit
                or rooms[r][c] == -1):
                return
            visit.add((r, c))
            q.append([r,c])
    
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.append((r,c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist #popping gate from q
                addRoom(r +1, c)
                addRoom(r -1, c)
                addRoom(r, c +1)
                addRoom(r, c -1)
            dist += 1 # for next iter all rooms will be 1 dist away from gate

'''
time O(m*n)
space O(m*n) ???
'''