class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        winlen = 0

        seen = set()

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                winlen = max(winlen, r-l+1)
            else:
                while l < r and s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
            r += 1
        
        return winlen