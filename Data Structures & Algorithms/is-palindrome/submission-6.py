class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s)-1
        s = s.lower()
        alph = 'qwertyuiopasdfghjklzxcvbnm0123456789'

        while p1<p2:
            while s[p1] not in alph and p1 < p2:
                p1 += 1
            while s[p2] not in alph and p2 > p1:
                p2 -= 1
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        
        return True
