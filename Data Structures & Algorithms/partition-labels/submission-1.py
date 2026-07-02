class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex = {}
        for i in range(len(s)):
            lastindex[s[i]] = i
        
        res = []
        size = end = 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, lastindex[c])

            if end==i:
                res.append(size)
                size = 0
        return res
            