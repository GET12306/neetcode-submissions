class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0

        while l+k <= len(nums):
            res.append(max(nums[l:l+k]))
            l += 1
        return res
