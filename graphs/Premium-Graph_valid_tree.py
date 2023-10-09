class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        if not n:
            return True
        
        adjacency = {i:[] for i in range(n)} 
        for e1, e2 in edges:
            adjacency[e1].append(e2)
            adjacency[e2].append(e1)
        
        visited = ()
        def dfs(vertex, prev):
            if vertex in visited:
                return False

            visited.add(vertex)
            for e in adjacency[vertex]:
                if e == prev: # ignoring edge that loops back to parent bc given undirected graph
                    continue
                if not dfs(e, vertex): #detected loop from dfs base case
                    return False 
            return True #bc no loop detected (but it could be have disconnected vertices)
        
        return dfs(0, -1) and len(visited) == n # make sure graph is tree (no loops and all v are connected)