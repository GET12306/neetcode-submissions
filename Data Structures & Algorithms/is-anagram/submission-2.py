class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cs, ct = {}, {}

        for r in s:
            cs[r] = cs.get(r, 0) + 1
        for r in t:
            ct[r] = ct.get(r, 0) + 1
        return cs == ct
