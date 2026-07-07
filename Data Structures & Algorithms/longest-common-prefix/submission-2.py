class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = 201
        minindex = -1
        for i, s in enumerate(strs):
            if len(s) < minlen:
                minindex = i
                minlen = len(s)
        
        if minlen==0: return ""

        minstr = strs[minindex]

        minstrchar = []
        for i in range(minlen):
            minstrchar.append(minstr[i])
        print(minstrchar, minstr)
        
        maxpre = minlen
        for s in strs:
            if s == minstr: continue
            for i in range(minlen):
                if s[i] != minstrchar[i]:
                    maxpre = min(maxpre, i-1)
        
        return ''.join(minstrchar[:maxpre+1])

        
                    