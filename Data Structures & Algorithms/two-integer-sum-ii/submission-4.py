class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        need = {}

        for i, num in enumerate(numbers):
            diff = target - num
            if diff in need.keys():
                return [need[diff]+1, i+1]
            need[num] = i