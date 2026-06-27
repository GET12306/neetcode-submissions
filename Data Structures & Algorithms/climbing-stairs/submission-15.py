class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        if n<=2: return n
        
        def recursive(k):
            if k in memo.keys(): return memo[k]
            if k<=2: return k
            memo[k] =recursive(k-1)+recursive(k-2)

            return memo[k]
        
        return recursive(n)
        