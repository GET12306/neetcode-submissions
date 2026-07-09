class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        where_appear = {}

        for i, num in enumerate(nums):
            if num in where_appear.keys():
                if i-where_appear[num] <= k:
                    return True
                else:
                    where_appear[num] = i
            where_appear[num] = i
        
        return False