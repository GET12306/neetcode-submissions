class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        res = []
        if len(strs)==1: 
            res.append(strs)
            return res
        
        for i, s in enumerate(strs):
            ss = ''.join(sorted(s))
            seen[ss].append(i)
            
        for indexlist in seen.values():
            temp = []
            for i in indexlist:
                temp.append(strs[i])
            res.append(temp)


        return res