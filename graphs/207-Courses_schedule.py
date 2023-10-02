class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # creatind adjacency list map
        preAdjMap = { c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preAdjMap[crs].append(pre)
        
        # visited set for courses in dfs path
        visited = set()

        def dfs(crs):
            if crs in visited: # to detect loop, so cannot be completed
                return False
            if preAdjMap[crs] == []:
                return True
            
            visited.add(crs)
            for pre in preAdjMap[crs]:
                if not dfs(pre):
                    return False
            preAdjMap[crs] = []
            visited.remove(crs)
            return True
            
        for crs in range(numCourses):
            if not dfs(crs): 
                return False    
        return True
'''
time O(v + e) v = len(numCourses) e = len(prereq)
space O(v + e) v = len(numCourses) e = len(prereq)
'''
