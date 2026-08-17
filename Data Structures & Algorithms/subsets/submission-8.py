class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def back(sub: list, i):
            if i >= len(nums):
                res.append(sub.copy())
                return
            
            sub.append(nums[i])
            back(sub, i+1)
            sub.remove(nums[i])
            back(sub, i+1)
        
        back([], 0)
        return res