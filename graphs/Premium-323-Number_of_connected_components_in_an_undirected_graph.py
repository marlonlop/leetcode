class Solution:
    def countComponents(self, n, edges):
        par = [i for i in range(n)]
        rank = [1] * n # rank = [1 for _ in range(n)]

        def find():
            res = n1
            while res != par[res]:
                par[res] = par[par[n]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res
