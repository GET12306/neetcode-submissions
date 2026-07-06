class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {0:0, 1:0, 2:0}
        for num in nums:
            count[num] += 1
        a, b, c = count[0], count[1], count[2]
        for i in range(a):
            nums[i] = 0
        for i in range(a, a+b):
            nums[i] = 1
        for i in range(a+b, len(nums)):
            nums[i] = 2
        