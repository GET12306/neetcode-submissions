class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        seen = []
        for num in nums:
            if num!=val:
                seen.append(num)
        k = len(seen)
        for i in range(k):
            nums[i] = seen[i]
        # for i in range(k, len(nums)):
        #     nums[i] = 0
        return k