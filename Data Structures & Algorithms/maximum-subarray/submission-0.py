class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]

        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur += nums[j]
                res = max(cur, res)
        return res