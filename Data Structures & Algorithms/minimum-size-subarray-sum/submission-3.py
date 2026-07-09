class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0
        if sum(nums) == target: return len(nums)
        # if len(nums) == 1: return 1

        minlen = len(nums) + 1
        l, r = 0, 0

        while r < len(nums):
            cur = sum(nums[l:r+1])
            if cur < target:
                r += 1
            else:
                minlen = min(r-l+1, minlen)
                l += 1

        return minlen