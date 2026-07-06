class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return nums[0]
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            if count[num] > n/2:
                return num

        for k in count.keys():
            if count[k] > n/2:
                return k