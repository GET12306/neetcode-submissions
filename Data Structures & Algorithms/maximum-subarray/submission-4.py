class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum, cur = nums[0], 0

        for num in nums:
            if cur < 0:
                cur = 0
            cur += num
            maxsum = max(cur, maxsum)
        return maxsum