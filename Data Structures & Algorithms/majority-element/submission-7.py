class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        n = len(nums)
        print(n)
        for k in count.keys():
            if count[k] > n/2:
                return k