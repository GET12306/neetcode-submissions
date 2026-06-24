class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curmin, curmax = 0, 0

        for num in nums:
            tmp = curmax + num
            
            curmax = max(num+curmax, num+curmin, num)
            curmin = min(tmp, num+curmin, num)
            
            res = max(res, curmax)
        
        return res