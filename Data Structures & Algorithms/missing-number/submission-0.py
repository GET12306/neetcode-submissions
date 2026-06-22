class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        if nums[0] != 0:
            return 0
        if nums[-1] != n:
            return n
        
        for i in range(n-1):
            if nums[i]+1 != nums[i+1]:
                return i+1
