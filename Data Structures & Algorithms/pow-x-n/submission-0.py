class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1.0
        
        res = 1.0
        if n > 0:
            for _ in range(n):
                res *= x
            return res
        else:
            for _ in range(abs(n)):
                res *= x
        
            return 1/res