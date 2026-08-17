class UnionFind:
    def __init__(self, n):
        # parent[i] 表示 i 的父节点
        # 初始时每个节点的父节点都是自己
        self.parent = list(range(n))

        # size[i] 表示以 i 为根的集合大小
        self.size = [1] * n

        # 当前连通分量数量
        self.count = n

    def find(self, x):
        """找到 x 所在集合的根节点"""
        if self.parent[x] != x:
            # 路径压缩
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        """合并 a 和 b 所在的集合"""
        root_a = self.find(a)
        root_b = self.find(b)

        # 已经属于同一个集合
        if root_a == root_b:
            return False

        # 按集合大小合并：小树挂到大树下面
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]

        self.count -= 1
        return True

    def connected(self, a, b):
        """判断 a 和 b 是否属于同一个集合"""
        return self.find(a) == self.find(b)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)

        for u, v in edges:
            same_root = uf.union(u, v)
            if not same_root:
                return False
        
        
        return True if uf.count == 1 else False
            

