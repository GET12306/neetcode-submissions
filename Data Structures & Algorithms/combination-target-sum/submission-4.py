class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []

        def back(i, cursum):
            if cursum == target:
                res.append(sub.copy())
                return
            elif cursum > target or i >= len(nums):
                return

            sub.append(nums[i])
            back(i, cursum+nums[i])
            
            sub.pop()
            back(i+1, cursum)
        
        back(0, 0)
        return res

