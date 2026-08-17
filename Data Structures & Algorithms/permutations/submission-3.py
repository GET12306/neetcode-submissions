class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def back(cur, used: list[bool]):
            if sum(used) == n:
                res.append(cur.copy())
                return

            for i, use in enumerate(used):
                if not use:
                    cur.append(nums[i])
                    used[i] = True
                    back(cur, used)
                    
                    cur.pop()
                    used[i] = False
                    


        back([],[False] * n)
        return res