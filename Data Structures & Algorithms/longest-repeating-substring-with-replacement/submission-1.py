class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        max_char = 0
        max_len = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_char = max(count[s[r]], max_char)

            while (r-l+1) - max_char > k:
                count[s[l]] -= 1
                l += 1
                # max_char = max(count[s[r]], max_char)
            
            max_len = max(max_len, r-l+1)

        return max_len