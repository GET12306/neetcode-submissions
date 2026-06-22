class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []

        def back(i, sub):
            if i == len(nums):
                res.append(sub.copy())
                return
            
            sub.append(nums[i])
            back(i+1, sub)
            sub.pop()
            back(i+1, sub)

        back(0, [])
        return res