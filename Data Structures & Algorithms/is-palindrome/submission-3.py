class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s) - 1
        s = s.lower()
        ascii_chr = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
        while p1 != p2:
            while p1<p2 and s[p1] not in ascii_chr:
                p1 += 1
            while p2>p1 and s[p2] not in ascii_chr:
                p2 -= 1
            if p1 >= p2:
                break
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True
