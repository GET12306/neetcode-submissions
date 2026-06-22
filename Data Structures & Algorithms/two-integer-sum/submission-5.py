class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}

        for i, val in enumerate(nums):
            if val in need:
                return [need[val], i]
            need[target-val] = i