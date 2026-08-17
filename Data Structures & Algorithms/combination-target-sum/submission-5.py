class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def back(sub: list, i, cursum):
            if cursum > target or i >= len(nums):
                return
            if cursum == target:
                res.append(sub.copy())
                return
            
            sub.append(nums[i])
            back(sub, i, cursum+nums[i])
            sub.pop()
            back(sub, i+1, cursum)
        
        back([], 0, 0)
        return res