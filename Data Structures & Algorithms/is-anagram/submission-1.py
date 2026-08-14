class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for r in s:
            if r not in t:
                return False
            t = t.replace(r, '', 1)
        
        return True
        