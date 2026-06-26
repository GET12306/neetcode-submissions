class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def back(i, cur):
            if sum(cur) == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or sum(cur)>target:
                return

            cur.append(candidates[i])
            back(i+1, cur)
            cur.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            back(i+1, cur)
        
        back(0, [])
        return res

