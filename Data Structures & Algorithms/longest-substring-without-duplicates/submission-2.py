class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mlen = 0
        l = r = 0
        seen = set()

        while r < len(s):
            if s[r] not in seen:
                mlen = max(mlen, r-l+1)
                seen.add(s[r])
                r += 1
            else:
                while s[r] in seen and l < r:
                    seen.remove(s[l])
                    l+=1
                        
        return mlen