class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        pos = {}

        for r in range(len(s)):
            if s[r] in pos:
                l = max(l, pos[s[r]] + 1)
            res = max(res, r-l+1)
            pos[s[r]] = r

        return res