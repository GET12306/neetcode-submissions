class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        nums.sort()

        def back(i):
            if i >= len(nums) or sum(sub) > target:
                return
            if sum(sub)==target:
                res.append(sub.copy())
                return
            
            sub.append(nums[i])
            back(i)
            sub.pop()
            back(i+1)
        
        back(0)
        return res
