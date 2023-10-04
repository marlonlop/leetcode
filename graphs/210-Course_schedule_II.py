class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency = {c : [] for c in range(numCourses)}
        for crs, preq in prerequisites:
            adjacency[crs].append(preq)
        
        # set for courses fully visited
        # set for courses in current cycle, but fully traversed (in visited)
        visited, cycle = set(), set()
        # output
        out = []

        def dfs(crs):
            if crs in visited:
                return True
            if crs in cycle:
                return False
            
            cycle.add(crs)
            for pre in adjacency[crs]:
                if not dfs(pre): # same as if dfs(crs) == False:
                    return False
            out.append(crs)
            visited.add(crs)
            cycle.remove(crs)
            return True
        
        for crs in adjacency: # same as adjacency.keys()
            if not dfs(crs): # same as if dfs(crs) == False:
                return []
        return out