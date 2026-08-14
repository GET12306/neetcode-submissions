class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in need.keys():
                return [need[diff], i]
            need[num] = i