class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        squ = self.calsqu(n)
        seen.add(squ)
        while squ != 1:
            if squ==4:
                return False
            squ = self.calsqu(squ)
            if squ in seen:
                return False
            seen.add(squ)
        return True

    def calsqu(self, num):
        output = 0
        while num:
            dig = num % 10
            dig = dig ** 2
            output += dig
            num = num // 10
        return output
