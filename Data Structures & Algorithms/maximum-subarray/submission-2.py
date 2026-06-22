class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum, cursum = nums[0], 0
        for i in range(len(nums)):
            if cursum < 0:
                cursum = 0
            cursum += nums[i]
            maxsum = max(maxsum, cursum)
        return maxsum