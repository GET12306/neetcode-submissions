class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False      
        self.parent[root_b] = root_a
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for u, v in edges:
            if not uf.union(u-1,v-1):
                return [u, v]