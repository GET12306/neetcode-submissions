class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}
        for i, num in enumerate(nums):
            curneed = target-num
            if curneed in need.keys():
                return [need[curneed], i]
            need[num] = i