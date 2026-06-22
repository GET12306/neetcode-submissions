class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def back(cur, visit):
            if len(cur)==len(nums):
                res.append(cur.copy())
                return

            for j in range(len(nums)):
                if nums[j] in visit:
                    continue
                cur.append(nums[j])
                visit.add(nums[j])
                back(cur, visit)
                cur.pop()
                visit.remove(nums[j])



        back([], set())
        return res
