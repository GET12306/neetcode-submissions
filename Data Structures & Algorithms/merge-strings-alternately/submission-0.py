class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        n1, n2 = len(word1), len(word2)
        res = ''
        is1 = True
        while p1<n1 and p2<n2:
            if is1:
                res += word1[p1]
                p1 += 1
                is1 = False
            else:
                res += word2[p2]
                p2 += 1
                is1 = True
        
        if p1 < n1: 
            res += word1[p1:]
        elif p2< n2: 
            res += word2[p2:]

        return res